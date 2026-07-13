"""
Image helper functions for album artwork

Getting the URl, using request module with .content to convert that url to raw bytes, then using ByteIO to convert them 
bytes to a file-like object and then using pillow to read and create the file-like object to a image for image.open() can
read the file.  
"""


from io import BytesIO
import requests
from PIL import Image, ImageOps

def download_image(image_url:str) -> Image.Image:
	response = requests.get(image_url, timeout=10)
	response.raise_for_status()
	return Image.open(BytesIO(response.content)).convert("RGB")

def resize_for_matrix(image:Image.Image, width: int = 64, height: int = 64) -> Image.Image:
	return ImageOps.fit(
			image, 
			(width, height),
			method=Image.Resampling.LANCZOS, 
			centering=(0.5, 0.5),
		) 
