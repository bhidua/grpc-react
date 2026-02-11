import grpc
from concurrent import futures
import time

from book_transaction import book_transaction_pb2
from book_transaction import book_transaction_pb2_grpc

from db.modify_book import list_book_borrow_transactions

class BookTransactionServiceServicer(book_transaction_pb2_grpc.BookTransactionServiceServicer):
    """Implements the BookTransactionService service definition."""

    def ListBookTransactions(self, request, context):
        """
        Processes a BookTransactionRequest and returns a TransactionResponse.
        """
        print(f"Received request for info for listBookTransaction:")
        
        return list_book_borrow_transactions(1,10)
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_transaction_pb2_grpc.add_BookTransactionServiceServicer_to_server(BookTransactionServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051")
    try:
        while True:
            time.sleep(86400) # One day
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
