from concurrent import futures
import logging

import grpc
import RPC_pb2_grpc
import RPC_pb2
import PB_pb2
# import RPC__pb2

# book = RPC__pb2.Book()
# book.id = "1"
# book.title = "Charlotte"
# book.author = "White"
# book.year = 1952

# book.genre = RPC__pb2.Book.Genre.COMEDY


# book2 = RPC__pb2.Book()
# book2.id = "2"
# book2.title = "Little Women"
# book2.author = "Louisa May Alcott"
# book2.year = 1983

# book.genre = RPC__pb2.Book.Genre.ROMANCE

database = {
    "1": PB_pb2.Book(isbn="1", title="Charlotte", author="White", year=1952, genre=PB_pb2.COMEDY),
    "2": PB_pb2.Book(isbn="2", title="LittleWomen", author="Alcott", year=1983, genre=PB_pb2.ROMANCE)
}


class InventoryService(RPC_pb2_grpc.InventoryServiceServicer):

    def GetBook(self, request, context):
        print(database)
        book = database[request.isbn]
        response = RPC_pb2.GetBookSearchResponse(isbn=book.isbn, title=book.title, author=book.author, genre=book.genre, year=book.year)
        return response

    def CreateBook(self, request, context):
        if request.isbn in database:
            response = RPC_pb2.CreateBookCreateResponse(result=0)
            return response

        newBook = PB_pb2.Book(isbn=request.isbn, title=request.title, author=request.author, year=request.year, genre=request.genre)
        database[request.isbn] = newBook

        response = RPC_pb2.CreateBookCreateResponse(result=1)
        return response

    # def CreateBook(self, request, context):
    #     return super().CreateBook(request, context)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    RPC_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()