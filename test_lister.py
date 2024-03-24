from unittest import mock
from lister import MovieLister
from movies import Movie

def test_lister():
    spielberg = [
        Movie(year=1979, name="1941", director="Spielberg"),
    ]
    movie_finder_mock = mock.MagicMock()
    movie_finder_mock.find_all.return_value = spielberg
    movie_lister = MovieLister(finder=movie_finder_mock)

    spielberg_movies = movie_lister.movies_directed_by('Spielberg')

    movie_finder_mock.find_all.assert_called_once()
    assert len(spielberg_movies) > 0
    assert all(movie.director == 'Spielberg' for movie in spielberg_movies)
