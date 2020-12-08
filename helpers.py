from numba import jit

@jit
def number_is_bounded_by_mandelbrot(c, iterations, z=0.0j, iteration=0):
    if iteration == iterations:
        return 0

    if (z.real ** 2 + z.imag ** 2) > 4:
        return iteration + 1

    z = z*z + c
    return number_is_bounded_by_mandelbrot(c, iterations, z, iteration + 1)

def hex_from_rgb(r,g,b):
    return '#%02x%02x%02x' % (r,g,b)

def get_color(iterations, rgb=False):
    values = [0, 32, 64, 128]

    b = values[iterations % 4]
    g = values[(iterations // 4) % 4] 
    r = values[(iterations // 16) % 4]
        
    return (r,g,b) if rgb else hex_from_rgb(r,g,b)

def draw_from_iterations_array(canvas, iterations_array, width, option, color="#000000"):
    
    # Option 1 draws the edge of the mandelbrot set
    if option == 1:
        for pixel in range(len(iterations_array)):
            if iterations_array[pixel] > 17:
                x = pixel % width
                y = pixel // width
                canvas.create_rectangle(x, y, x, y, outline=color)

    # Option 2 draws the inside of the mandelbrot set
    if option == 2:
        for pixel in range(len(iterations_array)):
            if iterations_array[pixel] == 0:
                x = pixel % width
                y = pixel // width
                canvas.create_rectangle(x, y, x, y, outline=color)

    # Option 3 draws whole mandelbrot set with a coloring scheme
    if option == 3:
        for pixel in range(len(iterations_array)):
            x = pixel % width
            y = pixel // width
            canvas.create_rectangle(x, y, x, y, outline=get_color(iterations_array[pixel]))

def get_area_variables(zoom_level):
    x_start = -2
    y_start = -1.5

    zoom_modifier = .25 * abs(zoom_level)

    if zoom_level == 0:
        x_width = 3
        y_height = 3
    elif zoom_level < 0:
        x_start = -2 - zoom_modifier
        y_start = -1.5 - zoom_modifier
        x_width = 3 + 2 * zoom_modifier
        y_height = 3 + 2 * zoom_modifier
    else :
        x_width = 3 - zoom_modifier
        y_height = 3 - zoom_modifier

    return x_start, y_start, x_width, y_height 
    