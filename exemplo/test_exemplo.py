from re import T
import unittest
import requests


class TestExemplo(unittest.TestCase):
    def testa_api_rest(self):
        self.assertEqual(True, requests.get('https://jsonplaceholder.typicode.com/posts/1').ok)
        
        

if __name__ == '__main__':
    unittest.main()