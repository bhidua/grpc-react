import grpc
import book_pb2
import book_pb2_grpc

def run():
    # Establish a connection channel to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = book_pb2_grpc.BookServiceStub(channel)
        
        # Call the RPC method CreateBook
        request = book_pb2.CreateBookRequest(name="example")
        response = stub.CreateBook(request)

        # Process the response data
        if response.is_book_created:
            print(f"gRPC response received:")
            print(f"  Success: {response.is_book_created}")
            # print(f"  Value: {response.value}")
        else:
            print(f"gRPC request failed: {response.is_book_created}")
            
            
         # Call the RPC method UpdateBook
        requestUpdate = book_pb2.UpdateBookRequest(id="1")
        responseUpdate = stub.UpdateBook(requestUpdate)

        # Process the response data
        if responseUpdate.is_book_updated:
            print(f"gRPC response received:")
            print(f"  Success: {responseUpdate.is_book_updated}")
            # print(f"  Value: {response.value}")
        else:
            print(f"gRPC request failed: {responseUpdate.is_book_updated}")
            
            
            
            

if __name__ == '__main__':
    run()
