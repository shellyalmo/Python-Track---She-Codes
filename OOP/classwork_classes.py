"""Ex 1 (ex4)
"""
class Song:
    def __init__(self, title, artist, album, track_number):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number


class Album:
    pass

class Playlist:
    pass

class Artist:
    def __init__(self, name, list_of_songs, list_of_albums):
        self.name = name