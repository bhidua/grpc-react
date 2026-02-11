import grpc
from concurrent import futures
import time

import member_pb2
import member_pb2_grpc

class MemberServiceServicer(member_pb2_grpc.MemberServiceServicer):
    """Implements the MemberService service definition."""

    def CreateMember(self, request, context):
        """
        Processes a CreateMemberRequest and returns a CreateMemberResponse.
        """
        print(f"Received request for info: {request.name}")
        # Process the request and return data
        if request.name == "example":
            return member_pb2.CreateMemberResponse(
                is_member_created=True
            )
        else:
            context.set_details("Invalid request info")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return member_pb2.CreateMemberResponse(
                is_member_created=False
            )
            
    def UpdateMember(self, request, context):
        """
        Processes a UpdateMemberRequest and returns a UpdateMemberResponse.
        """
        print(f"Received request for info: {request.id}")
        # Process the request and return data
        if request.id == "1":
            return member_pb2.UpdateMemberResponse(
                is_member_updated=True
            )
        else:
            context.set_details("Invalid request info")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return member_pb2.UpdateMemberResponse(
                is_member_updated=False
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    member_pb2_grpc.add_MemberServiceServicer_to_server(MemberServiceServicer(), server)
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
