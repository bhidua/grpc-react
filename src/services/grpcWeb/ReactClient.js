// Example React component snippet
//import { BookServiceClient } from './book_grpc_web_pb';
import BookServicePackage from './book/book_grpc_web_pb';
import MemberServicePackage from './member/member_grpc_web_pb';
import BookTransactionServicePackage from './libraryBookTransaction/book_transaction_grpc_web_pb';

import { CreateBookRequest, UpdateBookRequest } from './book/book_pb';
import { CreateMemberRequest, UpdateMemberRequest } from './member/member_pb';
import { TransactionRequest } from './libraryBookTransaction/book_transaction_pb';


// import * as google_protobuf_timestamp_pb from 'google-protobuf/google/protobuf/timestamp_pb';
// import { useState } from 'react';


const { BookServiceClient } = BookServicePackage;
const { MemberServiceClient } = MemberServicePackage;
const { BookTransactionServiceClient } = BookTransactionServicePackage;

const bookClient = new BookServiceClient(process.env.REACT_APP_GRPC_API_URL); // Connect to the grpc-web proxy
const memberClient = new MemberServiceClient(process.env.REACT_APP_GRPC_API_URL); // Connect to the grpc-web proxy
const bookTransactionClient = new BookTransactionServiceClient(process.env.REACT_APP_GRPC_API_URL); // Connect to the grpc-web proxy


function grpcBookCreate(name, author) {
  const request = new CreateBookRequest();
  request.setName(name);
  request.setAuthor(author);
  return bookClient.createBook(request, {}, (err, response) => {
    if (response) {
      console.log(response.getIsBookCreated());
      return response.getIsBookCreated();
    } else {
      console.error(err);
    }
  });  
}
function grpcBookUpdate(id, name, author) {
  const request = new UpdateBookRequest();
  request.setId(id);
  request.setName(name);
  request.setAuthor(author);
  return bookClient.updateBook(request, {}, (err, response) => {
    if (response) {
      console.log(response.getIsBookCreated());
      return response.getIsBookUpdated();
    } else {
      console.error(err);
    }
  });
}
function grpcMemberCreate(name, phone) {
  const request = new CreateMemberRequest();
  request.setName(name);
  request.setPhone(phone);
  return memberClient.createMember(request, {}, (err, response) => {
    if (response) {
      console.log(response.getIsBookCreated());
      return response.getIsMemberCreated();
    } else {
      console.error(err);
    }
  });
}
function grpcMemberUpdate(id, name, phone) {
  const request = new UpdateMemberRequest();
  request.setId(id);
  request.setName(name);
  request.setPhone(phone);
  return memberClient.updateMember(request, {}, (err, response) => {
    if (response) {
      console.log(response.getIsMemberCreated());
      return response.getIsMemberUpdated();
    } else {
      console.error(err);
    }
  });
}

function grpcListBookTransaction() {
  return new Promise((resolve, reject) => {
    const request = new TransactionRequest();
      bookTransactionClient.listBookTransactions(request, {}, (err, response) => {
        if (err) { 
          reject(err); 
        } 
        else { 
          resolve(response); 
        }
      });
    });
}

export { grpcBookCreate, grpcBookUpdate, grpcMemberCreate, grpcMemberUpdate, grpcListBookTransaction };
