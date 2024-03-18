class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if Song.genre_count.get(self.genre):
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if Song.artist_count.get(self.artist):
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
            Song.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        genre_count = {}
        for song in cls.genre_count:
            genre_count[song] = cls.genre_count.get(song, 0)
        return genre_count

    @classmethod
    def add_to_artist_count(cls):
        artist_count = {}
        for song in cls.artist_count:
            artist_count[song] = cls.artist_count.get(song, 0)
        return artist_count
