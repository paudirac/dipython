from lister import MovieLister


def test_lister():
    lister = MovieLister()
    spielberg_movies = lister.movies_directed_by('Spielberg')
    assert len(spielberg_movies) > 0
    assert all(movie.director == 'Spielberg' for movie in spielberg_movies)
