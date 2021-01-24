from settings import settings

# if pillow is installed, this function is defined and can be used to create an image of the mandelbrot set
if settings["pil_installed"]:
    from PIL import Image, ImageTk

    def get_mandelbrot_image(pixel_array, width, height):
        # NOTE: RGBA is used to get a transparent background
        image = Image.new(mode="RGBA", size=(width,height))
        image.putdata(pixel_array)

        return ImageTk.PhotoImage(image)

# make sure the function works even when numba is not installed
# numba adds the compiler option "jit" to make a function run faster
# NOTE: z=0.0j stands for z = 0+0i
if settings["numba_installed"]:
    from numba import jit

    @jit
    def number_is_bounded_by_mandelbrot(c, iterations, z=0.0j, iteration=0):
        if iteration == iterations:
            return 0

        if (z.real ** 2 + z.imag ** 2) > 4:
            return iteration + 1

        z = z*z + c
        return number_is_bounded_by_mandelbrot(c, iterations, z, iteration + 1)
else:
    def number_is_bounded_by_mandelbrot(c, iterations, z=0.0j, iteration=0):
        if iteration == iterations:
            return 0

        if (z.real ** 2 + z.imag ** 2) > 4:
            return iteration + 1

        z = z*z + c
        return number_is_bounded_by_mandelbrot(c, iterations, z, iteration + 1)

# simple function that converts rgb to hex
def rgb_to_hex(r,g,b):
    return '#%02x%02x%02x' % (r,g,b)

# simple function that converts hex to rgba
def hex_to_rgba(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    return (r,g,b, 255)

# Daniel
# This is the function responsible for the special option
# the rgb parameter indicates if it is for a canvas or an image
def get_special_color(iterations, rgb=False):
    values = [0, 32, 64, 128]

    b = values[iterations % 4]
    g = values[(iterations // 4) % 4] 
    r = values[(iterations // 16) % 4]
        
    return (r,g,b) if rgb else rgb_to_hex(r,g,b)

# this function processes each pixel of the mandelbrot set
def process_iterations_array(mandelbrot, fast_mode, canvas):
    # if fast mode is true, the mandelbrot will be processed for an image
    # otherwise the mandelbrot is drawn on the canvas
    # NOTE: callback is the function that is executed for each pixel
    if fast_mode:
        # initialize an empty pixel array
        pixel_array = [(255,255,255, 0)] * (mandelbrot.pixel_width * mandelbrot.pixel_height)

        def change_pixel(pixel, hex_color):
            pixel_array[pixel] = hex_to_rgba(hex_color)
        callback = change_pixel
    else:
        def draw_pixel_on_canvas(pixel, color):
            x = pixel % mandelbrot.pixel_width
            y = pixel // mandelbrot.pixel_width
            canvas.create_rectangle(x, y, x, y, outline=color)
        callback = draw_pixel_on_canvas
    
    # Daniel
    # Option 1 draws the edge of the mandelbrot set
    if mandelbrot.option == 1:
        for pixel in range(len(mandelbrot.iterations_array)):
            if mandelbrot.iterations_array[pixel] > 17:
                callback(pixel, mandelbrot.color)
    
    # Daniel
    # Option 2 draws the inside of the mandelbrot set
    elif mandelbrot.option == 2:
        for pixel in range(len(mandelbrot.iterations_array)):
            if mandelbrot.iterations_array[pixel] == 0:
                callback(pixel, mandelbrot.color)
                
    # Daniel
    # Option 3 draws the whole mandelbrot set with a special coloring scheme
    elif mandelbrot.option == 3:
        for pixel in range(len(mandelbrot.iterations_array)):
            color = get_special_color(mandelbrot.iterations_array[pixel])
            callback(pixel, color)

    if fast_mode:
        return pixel_array
    
