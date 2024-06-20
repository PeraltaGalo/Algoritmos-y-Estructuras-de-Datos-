import bisect

class Song:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __repr__(self):
        return f"Song(title='{self.title}', artist='{self.artist}', year={self.year})"


def sort_songs(songs, key):
    return sorted(songs, key=key)

def has_songs_by_artists(songs, artists):
    return {artist: any(song.artist == artist for song in songs) for artist in artists}


def songs_by_artist(songs, artist):
    return [song for song in songs if song.artist == artist]


def add_and_sort_song(songs, new_song):
    bisect.insort(songs, new_song, key=lambda song: song.title)


def count_songs_by_artist(songs, artist):
    return sum(1 for song in songs if song.artist == artist)


def show_songs_info(songs, titles):
    return [song for song in songs if song.title in titles]


songs = [
    Song("Fake tales of San Francisco", "Arctic Monkeys", 2006),
    Song("Black hole sun", "Soundgarden", 1994),
    Song("Californication", "Red Hot Chili Peppers", 1999),
    Song("Otherside", "Red Hot Chili Peppers", 1999),
    Song("Show Me How to Live", "Audioslave", 2002),
    Song("Paint It Black", "The Rolling Stones", 1966),
    Song("Smells Like Teen Spirit", "Nirvana", 1991),
    Song("Come As You Are", "Nirvana", 1991),
]


print("\nOrdenado por canción:")
sorted_by_title = sort_songs(songs, key=lambda song: song.title)
print(sorted_by_title)

print("\nOrdenado por banda o artista:")
sorted_by_artist = sort_songs(songs, key=lambda song: song.artist)
print(sorted_by_artist)

print("\nOrdenado por año de lanzamiento:")
sorted_by_year = sort_songs(songs, key=lambda song: song.year)
print(sorted_by_year)


print("\nExisten canciones de Audioslave y Rolling Stones:")
exists = has_songs_by_artists(songs, ["Audioslave", "The Rolling Stones"])
print(exists)


print("\nCanciones de Nirvana:")
nirvana_songs = songs_by_artist(songs, "Nirvana")
print(nirvana_songs)


new_song = Song("Scar Tissue", "Red Hot Chili Peppers", 1999)
add_and_sort_song(songs, new_song)
print("\nListado ordenado por nombre de canción después de agregar 'Scar Tissue':")
print(sort_songs(songs, key=lambda song: song.title))


print("\nNúmero de canciones de Red Hot Chili Peppers:")
rhcp_count = count_songs_by_artist(songs, "Red Hot Chili Peppers")
print(rhcp_count)


print("\nInformación de las canciones 'Fake tales of San Francisco' y 'Black hole sun':")
specific_songs_info = show_songs_info(songs, ["Fake tales of San Francisco", "Black hole sun"])
print(specific_songs_info)
