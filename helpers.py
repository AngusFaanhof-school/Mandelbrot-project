from numba import jit

@jit
def number_is_bounded_by_mandelbrot(real, imaginary, iterations):
    c = complex(real, imaginary)
    z = 0.0j

    iter = 0
    while iter <= iterations:
        iter += 1
        z = z*z + c
        if (z.real ** 2 + z.imag ** 2) > 4:
            return iter + 1

    return 0

def draw_from_pixel_array(canvas, image_array, width):
    length = len(image_array)

    for p in range(length):
        if image_array[p] == 0:
            x = p % width
            y = p // width
            canvas.create_rectangle(x, y, x, y, outline="white")

def get_pixel_array(image_array, width, option):
    length = len(image_array)
    pixel_array = [0] * length

    if option == 1:
        for p in range(length):
            if image_array[p] != 0:
                pixel_array[p] = (255,255,255)
    
    if option == 2:
        for p in range(length):
            if image_array[p] < 20:
                pixel_array[p] = (255,255,255)

    return pixel_array

def get_summary_from_settings(settings):
    summary = ""

    for setting in settings.keys():
        summary += f"_{settings[setting]}"

    return summary

    exit()
