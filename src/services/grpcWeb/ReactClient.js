// Example React component snippet
//import { BookServiceClient } from './book_grpc_web_pb';
import BookServicePackage from './book_grpc_web_pb';
import { CreateBookRequest } from './book_pb';
import * as google_protobuf_timestamp_pb from 'google-protobuf/google/protobuf/timestamp_pb';
// import { useState } from 'react';


const { BookServiceClient } = BookServicePackage;

const bookClient = new BookServiceClient(process.env.REACT_APP_GRPC_API_URL); // Connect to the grpc-web proxy

function grpcBookCreate(data) {
  const bookGrpcService = (name, author) => {
    const request = new CreateBookRequest();
    request.setName(name);
    request.setAuthor(author);
    const now = new Date();
    const timestamp = google_protobuf_timestamp_pb.Timestamp.fromDate(now);
    request.setBorrowedTime(timestamp);
    request.setReturnedTime(timestamp);

    bookClient.createBook(request, {}, (err, response) => {
      if (response) {
        console.log(response.getIsBookCreated());
        return response.getIsBookCreated();
      } else {
        console.error(err);
      }
    });
  };
  return bookGrpcService(data);
  // return (
  //   <div>
  //     <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
  //     <button onClick={callBookGrpcService}>Create Book (gRPC)</button>
  //     <p>Server response: {message}</p>
  //   </div>
  // );
}
function grpcBookUpdate(data) {}
function grpcMemberCreate(data) {}
function grpcMemberUpdate(data) {}
function grpcListBookTransaction(data) {}
//export default BookGrpcComponent;

export { grpcBookCreate, grpcBookUpdate, grpcMemberCreate, grpcMemberUpdate, grpcListBookTransaction };
