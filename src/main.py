"""
This is the main, which will orchestrate all the modules created togther

"""

from spotify_client 	import create_spotify_client, get_current_track
from matrix_display 	import MatrixDisplay
from image_utils 	import download_image, resize_for_matrix
from PIL 		import Image

import time

def main():

	# create spotify client
	spotify_client 	= create_spotify_client()
	# create matrix display
	display = MatrixDisplay()
	# remember the last song ID so that can display
	Last_tracked_id = None
	# loop forever here:
	while True:
		# ask spotify for current track
		track = get_current_track(spotify_client)
		# check if anything is playing
		# if nothing is playing clear display
		if not track:
			Last_tracked_id = None
			display.clear()
			print("clearing!!!!!!")
			time.sleep(5)
			continue
		# Something is playing so download art, resize, and display it, and remember the song's ID
		if track["id"] != Last_tracked_id:
			Last_tracked_id = track["id"]
			image = download_image(track["album_art_url"])
			matrix_image = resize_for_matrix(image)
			display.display_image(matrix_image)
		# wait 2 seconds and repeat
		time.sleep(2)

if __name__ == "__main__":
    main()
