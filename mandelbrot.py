import numpy, time
from numba import jit
from PIL import Image


@jit
def mandelbrot(real, imaginary, iterations):
    c = complex(real, imaginary)
    z = 0.0j

    iter = 0
    while iter <= iterations:
        iter += 1
        z = z*z + c
        if (z.real ** 2 + z.imag ** 2) > 4:
            return False

    return True


class MandelbrotImage:
    def __init__(self, scale=500, iterations=50, x_start=-2, y_start=-1.5, x_width=3, y_height=3):
        self.scale = scale
        self.iterations = iterations
        self.x_start = x_start
        self.y_start = y_start
        self.x_width = x_width
        self.y_height = y_height

        self.fill_image_array()
    
    # @property
    # def meta_data(self):
    #     return {
    #         "scale": self.scale,
    #         "iterations": self.iterations,
    #         "x_start": self.x_start,
    #         "y_start": self.y_start,
    #         "x_width": self.x_width,
    #         "y_height": self.y_height,
    #     }

    def fill_image_array(self):
        start_time = time.time()
        image_array = numpy.zeros((self.scale, self.scale, 3), dtype=numpy.uint8)

        for row_index in range(self.scale + 1):
            real = self.x_start  + (row_index / self.scale) * self.x_width

            for column_index in range(self.scale + 1):
                global mandelbrot

                imaginary = self.y_start + (column_index / self.scale) * self.y_height
                value = mandelbrot(real, imaginary, self.iterations)
                if value:
                    image_array[column_index, row_index] = (255, 255, 255)

        self.image = Image.fromarray(image_array)
        print(time.time() - start_time)
