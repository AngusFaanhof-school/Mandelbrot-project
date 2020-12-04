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

def get_color(iterations):
    values = [0, 32, 64, 128]
    b = values[iterations % 4]
    g = values[(iterations // 4) % 4] 
    r = values[(iterations // 16) % 4]
        
    return '#%02x%02x%02x' % (r, g, b)

def draw_from_iterations_array(canvas, iterations_array, width, option):
    
    # full
    if option == 1:
        for pixel in range(len(iterations_array)):
            if iterations_array[pixel] == 0:
                x = pixel % width
                y = pixel // width
                canvas.create_rectangle(x, y, x, y, outline="red")

    # edge
    if option == 2:
        for pixel in range(len(iterations_array)):
            if iterations_array[pixel] > 20:
                x = pixel % width
                y = pixel // width
                canvas.create_rectangle(x, y, x, y, outline="red")

    # fancy
    if option == 3:
        for pixel in range(len(iterations_array)):
            x = pixel % width
            y = pixel // width
            canvas.create_rectangle(x, y, x, y, outline=get_color(iterations_array[pixel]))

def get_summary_from_settings(settings):
    summary = ""

    for setting in settings.keys():
        summary += f"_{settings[setting]}"

    return summary
