import webbrowser

class Movie(object):
    """
    This class provides a way to store
    movie-related information.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Constructs an instance of the class Movie.
        :inputs: title, storyline, URL for the movie poster image,
        URL for the YouTube trailer
        :outputs: a new instance/object of the class Movie
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        