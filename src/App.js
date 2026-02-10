// import logo from './logo.svg';
import { Routes, Route } from 'react-router-dom';
import './App.css'

import ListAndBorrowBook from './components/bookUpdation/ListAndBorrowBook';
import ListAndReturnBook from './components/bookUpdation/ListAndReturnBook';
import CreateBook from './components/bookUpdation/CreateBook';
import CreateMember from './components/memberUpdation/CreateMember';
import UpdateBook from './components/bookUpdation/UpdateBook';
import UpdateMember from './components/memberUpdation/UpdateMember';
import ListBookTransaction from './components/libraryBookTransaction/ListBookTransaction';

function App() {
  return (
    <div className="App">
      <div><h1>Library Management</h1></div>
      <div className="container">
      <div className="item"><a href="/borrowBook">Borrow Book</a></div>
      <div className="item"><a href="/returnBook">Return Book</a></div>
      <div className="item"><a href="/createbook">Create Book</a></div>
      <div className="item"><a href="/updatebook">Update Book</a></div>
      <div className="item"><a href="/createmember">Create Member</a></div>
      <div className="item"><a href="/updatemember">Update Member</a></div>
      <div className="item"><a href="/listbooktransaction">List Book Transactions</a></div>
      </div>
       <Routes>
          <Route path="/borrowbook" element={<ListAndBorrowBook/>} />
          <Route path="/returnbook" element={<ListAndReturnBook/>} />
          <Route path="/createbook" element={<CreateBook/>} />
          <Route path="/updatebook" element={<UpdateBook/>} />
          <Route path="/createmember" element={<CreateMember/>} />
          <Route path="/updatemember" element={<UpdateMember/>} />
          <Route path="/listbooktransaction" element={<ListBookTransaction/>} />
          <Route path="/" element={<ListBookTransaction/>} />
          <Route path="*" element={<h1>404: Not Found</h1>} />
        </Routes>
    </div>
  );
}

export default App;
