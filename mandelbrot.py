from numpy import zeros, uint8
from PIL import Image
from helpers import number_is_bounded_by_mandelbrot


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
        image_array = zeros((self.scale, self.scale, 3), dtype=uint8)

        for row_index in range(self.scale + 1):
            real = self.x_start  + (row_index / self.scale) * self.x_width

            for column_index in range(self.scale + 1):
                imaginary = self.y_start + (column_index / self.scale) * self.y_height

                value = number_is_bounded_by_mandelbrot(real, imaginary, self.iterations)

                if value:
                    image_array[column_index, row_index] = (255, 255, 255)

        self.image = Image.fromarray(image_array)
