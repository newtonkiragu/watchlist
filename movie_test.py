import unittest
from .models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the movie class
    '''

    def setUp(self):
        '''
        Setup method that will run before every test
        '''

        self.new_movie = Movie(1234,'Python must be crazy','A thrilling new python series','http://lorempixel.com/400/200',8.5,129993)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

if __name__ == '__main__':
    unittest.main()