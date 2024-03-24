#!/usr/bin/env python
import use_cases
from lister import MovieLister
from finder import MovieFinder

if __name__ == '__main__':
    finder = MovieFinder()
    lister = MovieLister(finder=finder)
    use_cases.print_movies_directed_by('Steven Spielbert', lister)
