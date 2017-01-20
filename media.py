import webbrowser

class Movie:
    """ Create a data structure to store your favorite movies,
    including movie title, storyline, box art URL and a YouTube link to the movie trailer.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        self.title = movie_title # Title of the movie
        self.storyline = movie_storyline # THe storyline
        self.poster_image_url = poster_image # The  poster image
        self.trailer_youtube_url = trailer  #Video trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
