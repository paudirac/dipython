from lister import IMovieLister

def print_movies_directed_by(director: str, lister: IMovieLister):
    spielberg_movies = lister.movies_directed_by('Steven Spielberg')
    print(spielberg_movies)
