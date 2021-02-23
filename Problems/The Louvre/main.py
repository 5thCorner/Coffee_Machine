class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


new_painting = Painting(str(input()), str(input()), str(input()))
print('"{}" by {} ({}) hangs in the {}.'.format(new_painting.title, new_painting.artist,
                                            new_painting.year, Painting.museum))
