"""
Spotify API helper functions.

"""


import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "user-read-currently-playing user-read--playback-state"

def create_spotify_client():
	return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

def get_current_track(sp):
	current_track = sp.current_user_playing_track()
	if not current_track or not current.get("item"):
		return None
	item = current["item"]
	return {
		"id": item["id"]
		"title": item["name"]
		"arist": item["arist"][0]["name"]
		"album": item["album"]["name"]
		"album_art_url": item["album"]["images"][0]["url"]
		"is_playing": current_track["is_playing"]
	}

