// import logo from './logo.svg';
import { Routes, Route } from 'react-router-dom';
import './App.css';

import CreateBook from './components/BookUpdation/CreateBook';
import CreateMember from './components/MemberUpdation/CreateMember';
import UpdateBook from './components/BookUpdation/UpdateBook';
import UpdateMember from './components/MemberUpdation/UpdateMember';
import ListBookTransaction from './components/LibraryBookTransaction/ListBookTransaction';

function App() {
  return (
    <div className="App">
      <div><h1>Library Management</h1></div>
      <div className="container">
      <div className="item"><a href="/createbook">Create Book</a></div>
      <div className="item"><a href="/updatebook">Update Book</a></div>
      <div className="item"><a href="/createmember">Create Member</a></div>
      <div className="item"><a href="/updatemember">Update Member</a></div>
      <div className="item"><a href="/listbooktransaction">List Book Transactions</a></div>
      </div>
       <Routes>
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
