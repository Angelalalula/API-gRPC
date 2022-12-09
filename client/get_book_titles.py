import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.append(os.path.join(os.path.dirname(SCRIPT_DIR), "service"))

import grpc
from service import PB_pb2, RPC_pb2_grpc, RPC_pb2
from inventory_client import Client

def GetBooks(client, isbn_list):
    
    book_list = []

    for isbn in isbn_list:
        book_list.append(client.GetBook(isbn).title)

    return book_list
    


if __name__ == "__main__":

    client = Client('localhost', 50051)
    books = GetBooks(client, ["1", "2"])

    for b in books:
        print(b.title)