"""
This code will display the image created from PILLOW function from the image_util.py code
It ONLY grabs the image and displays it.  IT DOES NOT SAVE IT, KNOW WHERE IT CAME FROM, OR MAKE ANY CHANGES
"""

from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions


class MatrixDisplay:
	def __init__(self):
		options = RGBMatrixOptions()
		options.rows = 64
		options.cols = 64
		options.chain_length = 1
		options.hardware_mapping = "adafruit-hat"
		options.gpio_slowdown = 6
		options.brightness = 65

		self.matrix = RGBMatrix(options=options)

	def display_image(self, image: Image.Image) -> None:
		image = image.convert("RGB")
		self.matrix.SetImage(image)

	def clear(self) -> None:
		self.matrix.clear()
