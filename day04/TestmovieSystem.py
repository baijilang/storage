import unittest
from unittest import TestCase
from ddt import ddt
from ddt import data
import warnings
from caseOfMovie import CaseOfMovie
from movieSystem import MovieManager

Database = CaseOfMovie()
data1 = CaseOfMovie.data1
data2 = CaseOfMovie.data2
data3 = CaseOfMovie.data3
data4 = CaseOfMovie.data4
data5 = CaseOfMovie.data5
data6 = CaseOfMovie.data6


@ddt
class TestMovieSystem(TestCase):

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.theater = MovieManager()

    @data(*data1)
    def test1_home(self, data_dic):
        code, text = self.theater.home()
        result = self.theater.find(text, 'home')
        self.assertEqual(data_dic['exception'], result)

    @data(*data2)
    def test2_login(self, data_dic):
        self.theater.home()
        code, text = self.theater.login(data_dic['uname'], data_dic['pwd'])
        result = self.theater.find(text, 'login')
        self.assertEqual(data_dic['exception'], result)

    @data(*data3)
    def test3_movie_list(self, data_dic):
        self.theater.home()
        self.theater.login(data_dic['uname'], data_dic['pwd'])
        code, text = self.theater.movie_list()
        result = self.theater.find(text, 'movie_list')
        self.assertEqual(data_dic['exception'], result)

    @data(*data4)
    def test4_query_movie(self, data_dic):
        self.theater.home()
        self.theater.login(data_dic['uname'], data_dic['pwd'])
        self.theater.movie_list()
        code, text = self.theater.query_movie(movie_name=data_dic['movieName'])
        result = self.theater.find(text, 'query_movie')
        self.assertEqual(data_dic['exception'], result)

    @data(*data5)
    def test5_movie_detail(self, data_dic):
        self.theater.home()
        self.theater.login(data_dic['uname'], data_dic['pwd'])
        self.theater.movie_list()
        self.theater.query_movie(movie_name=data_dic['movieName'])
        code, text = self.theater.query_detail()
        result = self.theater.find(text, 'query_detail')
        self.assertEqual(data_dic['exception'], result)

    @data(*data6)
    def test6_login_out(self, data_dic):
        self.theater.home()
        self.theater.login(data_dic['uname'], data_dic['pwd'])
        self.theater.movie_list()
        self.theater.query_movie(movie_name=data_dic['movieName'])
        self.theater.query_detail()
        code, text = self.theater.login_out()
        result = self.theater.find(text, 'login_out')
        self.assertEqual(data_dic['exception'], result)


if __name__ == "__main__":
    unittest.main()
