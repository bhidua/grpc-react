import grpc
import member_pb2
import member_pb2_grpc

def run():
    # Establish a connection channel to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = member_pb2_grpc.MemberServiceStub(channel)
        
        # Call the RPC method CreateMember
        request = member_pb2.CreateMemberRequest(name="example")
        response = stub.CreateMember(request)

        # Process the response data
        if response.is_member_created:
            print(f"gRPC response received:")
            print(f"  Success: {response.is_member_created}")
            # print(f"  Value: {response.value}")
        else:
            print(f"gRPC request failed: {response.is_member_created}")
            
            
         # Call the RPC method UpdateMember
        requestUpdate = member_pb2.UpdateMemberRequest(id="1")
        responseUpdate = stub.UpdateMember(requestUpdate)

        # Process the response data
        if responseUpdate.is_member_updated:
            print(f"gRPC response received:")
            print(f"  Success: {responseUpdate.is_member_updated}")
            # print(f"  Value: {response.value}")
        else:
            print(f"gRPC request failed: {responseUpdate.is_member_updated}")
            
            
            
            

if __name__ == '__main__':
    run()
