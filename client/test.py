
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append(os.path.join(os.path.dirname(SCRIPT_DIR), "service"))

import unittest
from unittest.mock import patch, Mock

from inventory_client import Client
from get_book_titles import GetBooks



class TestClient(unittest.TestCase):

    @patch('get_book_titles.Client')
    def test_get_books_no_server(self, client_mock):

        side_effect_database = {
            "1": Mock(title="Charlotte"), 
            "2": Mock(title="LittleWomen")
        }
        
        client_mock.GetBook.side_effect = lambda x: side_effect_database[x]

        self.assertEqual(GetBooks(client_mock, ["1", "2"]), ["Charlotte", "LittleWomen"])
    
    def test_get_books(self):

        self.assertEqual(GetBooks(Client('localhost', 50051), ["1", "2"]), ["Charlotte", "LittleWomen"])
    


if __name__ == "__main__":
    unittest.main()