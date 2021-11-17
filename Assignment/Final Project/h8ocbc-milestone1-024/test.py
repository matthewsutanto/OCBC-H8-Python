import app
import unittest

class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        app.connex_app.app.testing = True
        self.app = app.connex_app.app.test_client()

    def test_read_empty_movie(self):
        #test ketika id yang diinput tidak ada di database
        result = self.app.get('/api/movie/manage/8912')
        # Make your assertions
        self.assertEquals(result.status_code, 404)
    
    def test_read_movie_director(self):
        # test ketika mencoba mendapatkan nama director dari movies dengan id ke 45612
        result = self.app.get('/api/movie/manage/45612')
        # Make your assertions
        response = result.json
        director = response["directors"]["name"]
        self.assertEqual(director, "Mel Brooks")
        
    def test_read_director_revenue(self):
        # test ketika mencoba mendapatkan revenue dari film yang dibuat oleh director dengan id 6623
        result = self.app.get('/api/director/revenue/6623')
        # Make your assertions
        response = result.json
        self.assertEqual(response, 535692636)
    
    def test_read_director_department(self):
        # test ketika mencoba mendapatkan department dari director dengan id 6623
        result = self.app.get('/api/director/6623')
        # Make your assertions
        response = result.json
        director = response["department"]
        self.assertEqual(director, "Directing")
        
if __name__ == '__main__':
    unittest.main()