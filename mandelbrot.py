from PIL import Image
from helpers import number_is_bounded_by_mandelbrot
import time

class MandelbrotImage:
    def __init__(self, picture_width=500, picture_height=500, iterations=50, x_start=-2, y_start=-1.5, x_width=3, y_height=3):
        self.picture_width = picture_width
        self.picture_height = picture_height
        self.iterations = iterations
        self.x_start = x_start
        self.y_start = y_start
        self.x_width = x_width
        self.y_height = y_height

        self.fill_image_array()

    def fill_image_array(self):
        start_time = time.time()

        image_array = [(0,0,0)] * (self.picture_width * self.picture_height)
        height = int(self.picture_height / 2)

        for y in range(height + 1):
            imaginary = self.y_start + (y / self.picture_height) * self.y_height
            pixel_y = y * self.picture_width

            for x in range(self.picture_width):
                real = self.x_start  + (x / self.picture_width) * self.x_width

                value = number_is_bounded_by_mandelbrot(real, imaginary, self.iterations)
                if value:
                    image_array[pixel_y + x] = (255,255,255)
                    image_array[self.picture_height - pixel_y + x] = (255,255,255)

        self.image = Image.new("RGB", (self.picture_width, self.picture_height))
        self.image.putdata(image_array)

        print(time.time() - start_time)
