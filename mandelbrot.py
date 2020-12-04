from PIL import Image
from helpers import number_is_bounded_by_mandelbrot
import time

class Mandelbrot:
    def __init__(self, pixel_width, pixel_height, iterations=100, x_start=-2, y_start=-1.5, x_width=3, y_height=3):
        self.pixel_width = pixel_width
        self.pixel_height = pixel_height
        self.iterations = iterations
        self.x_start = x_start
        self.y_start = y_start
        self.x_width = x_width
        self.y_height = y_height

        self.fill_iterations_array()

    def fill_iterations_array(self):
        start_time = time.time()

        iterations_array = [0] * (self.pixel_width * self.pixel_height)

        for y in range(self.pixel_height):
            imaginary = self.y_start + (y / self.pixel_height) * self.y_height
            pixel_y = y * self.pixel_width

            for x in range(self.pixel_width):
                real = self.x_start  + (x / self.pixel_width) * self.x_width

                value = number_is_bounded_by_mandelbrot(real, imaginary, self.iterations)
                if value:
                    iterations_array[pixel_y + x] = value

        self.iterations_array = iterations_array

        print(time.time() - start_time)
