
import grpc
from service import RPC_pb2_grpc, RPC_pb2

class Client:


    def __init__(self, server_address='localhost', port=50051):
        self.channel = grpc.insecure_channel(str(server_address) + ":" + str(port))
        self.stub = RPC_pb2_grpc.InventoryServiceStub(self.channel)


    def CreateBook(self, isbn, title, author, genre, year):
        request = self.stub.CreateBook(RPC_pb2.CreateBookCreateRequest(isbn=isbn, title=title, author=author, genre=genre, year=year))
        return request


    def GetBook(self, isbn):
        # send the ISBN number to the search request and retrieve book from database
        response = self.stub.GetBook(RPC_pb2.GetBookSearchRequest(isbn=isbn))

        return response