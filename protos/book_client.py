from __future__ import print_function

import logging

import grpc
import PB_pb2
import RPC_pb2_grpc
import RPC_pb2


# given the Genre is of type enum, set converter from Genre to String and vice-versa for decoding and encoding
genreToString = {
    PB_pb2.HORROR: "Horror",
    PB_pb2.COMEDY: "Comedy",
    PB_pb2.ROMANCE: "Romance"
}

stringToGenre = {
    "Horror": PB_pb2.HORROR,
    "Comedy": PB_pb2.COMEDY,
    "Romance": PB_pb2.ROMANCE
}

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = RPC_pb2_grpc.InventoryServiceStub(channel)

        # take input from user, 1 to create new book, 2 to get info details about an existing book
        command = input("Input:\n [1] to create a new book\n [2] to get an existing book's details\n")
        if command == "1":
            isbn = input("\nInput the book ISBN\n")
            title = input("Input the book title\n")
            author = input("Input the book author\n")
            genre = stringToGenre[input("Input the book genre\n")]
            year = int(input("Input the book publishing year\n"))

            # send the details to create request and add new book to the database
            request = stub.CreateBook(RPC_pb2.CreateBookCreateRequest(isbn=isbn, title=title, author=author, genre=genre, year=year))
            if request.result:
                print("Book successfully created")
            else:
                print("Book creation failed")

        elif command == "2":
            isbn = input("\nInput the book's ISBN\n")
            
            # send the ISBN number to the search request and retrieve book from database
            response = stub.GetBook(RPC_pb2.GetBookSearchRequest(isbn=isbn))   
            print("\nTitle: " + response.title)
            print("Author: " + response.author)
            print("Genre: " + genreToString[response.genre])
            print("Publishing year: " + str(response.year))

if __name__ == '__main__':
    logging.basicConfig()
    run()