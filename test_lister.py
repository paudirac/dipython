from unittest import mock
from lister import MovieLister
from movies import Movie

def test_lister():
    spielberg = [
        Movie(year=1979, name="1941", director="Spielberg"),
    ]
    with mock.patch('lister.MovieFinder') as mocked_finder_class:
        mocked_finder_class.return_value.find_all.return_value = spielberg
        movie_lister = MovieLister()
        spielberg_movies = movie_lister.movies_directed_by('Spielberg')
        mocked_finder_class.return_value.find_all.assert_called_once()
        assert len(spielberg_movies) > 0
        assert all(movie.director == 'Spielberg' for movie in spielberg_movies)
