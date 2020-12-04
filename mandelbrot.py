from helpers import number_is_bounded_by_mandelbrot

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
        # create an array for each pixel. The value of each pixel is set to 0
        self.iterations_array = [0] * (self.pixel_width * self.pixel_height)

        # Go over each pixel in the y dimension
        for y in range(self.pixel_height):
            # Set the imaginary part of the complex number
            imaginary = self.y_start + (y / self.pixel_height) * self.y_height
            pixel_y = y * self.pixel_width

            # Go over each pixel in the x dimension
            for x in range(self.pixel_width):
                # Set the real part of the imaginary number
                real = self.x_start  + (x / self.pixel_width) * self.x_width

                value = number_is_bounded_by_mandelbrot(complex(real, imaginary), self.iterations)
                if value:
                    self.iterations_array[pixel_y + x] = value

                # Check if the value diverged
                if value:
                    # Set the pixel to the amount of iterations it took to diverge
                    self.iterations_array[pixel_y + x] = value