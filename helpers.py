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
            return False

    return True

def get_summary_from_settings(settings):
    summary = ""

    for setting in settings.keys():
        summary += f"_{settings[setting]}"

    return summary
