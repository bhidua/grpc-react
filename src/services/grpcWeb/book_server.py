import grpc
from concurrent import futures
import time

import book_pb2
import book_pb2_grpc

class BookServiceServicer(book_pb2_grpc.BookServiceServicer):
    """Implements the BookService service definition."""

    def CreateBook(self, request, context):
        """
        Processes a CreateBookRequest and returns a CreateBookResponse.
        """
        print(f"Received request for info: {request.name}")
        # Process the request and return data
        if request.name == "example":
            return book_pb2.CreateBookResponse(
                is_book_created=True
            )
        else:
            context.set_details("Invalid request info")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return book_pb2.CreateBookResponse(
                is_book_created=False
            )
            
    def UpdateBook(self, request, context):
        """
        Processes a UpdateBookRequest and returns a UpdateBookResponse.
        """
        print(f"Received request for info: {request.id}")
        # Process the request and return data
        if request.id == "1":
            return book_pb2.UpdateBookResponse(
                is_book_updated=True
            )
        else:
            context.set_details("Invalid request info")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return book_pb2.UpdateBookResponse(
                is_book_updated=False
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    book_pb2_grpc.add_BookServiceServicer_to_server(BookServiceServicer(), server)
    server.add_insecure_port('DESKTOP-F29H721:50051')
    server.start()
    print("Server started, listening on port 50051")
    try:
        while True:
            time.sleep(86400) # One day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
