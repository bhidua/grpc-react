import { useEffect, useState } from 'react';
import '../../App.css';
import {
  useReactTable,
  getCoreRowModel,
  getPaginationRowModel, // Import the pagination model
  flexRender,
  createColumnHelper,
} from '@tanstack/react-table';
import { grpcListBookTransaction } from '../../services/grpcWeb/ReactClient'

function ListBookTransaction() {   
  const [data,setData] = useState([]);
  const fetchBookTransactions = async () => {
        try {
          const response = await grpcListBookTransaction();
          const data = response.getTransactionsList().map(( txn ) =>  
            {    
              return {      
                book_name: txn.getBookName(),      
                is_book_available: txn.getIsBookAvailable(),      
                member_name: txn.getMemberName(),      
                borrowed_time: grpcTimestampToString(txn.getBorrowedTime()),      
                returned_time: grpcTimestampToString(txn.getReturnedTime())    
              }  
            });
          setData(data);
        } catch (err) {
          console.error(err);
        } finally {
          
        }
        function grpcTimestampToDate(ts) {
          if (!ts) return null;
          const seconds = ts.getSeconds();
          const nanos = ts.getNanos();
          // Convert seconds + nanos to milliseconds
          return new Date(seconds * 1000 + Math.floor(nanos / 1e6));
        }
        function grpcTimestampToString(ts) {
          const date = grpcTimestampToDate(ts);
          return date ? date.toLocaleString() : null;
        }
  }
  
  
  useEffect(() => {
    fetchBookTransactions();
  }, []);

  const handleBorrow = (row) => {
    // client.approve(request, {}, (err, response) => {
    //   if (err) {
    //     console.error("gRPC error:", err);
    //     return;
    //   }
      // console.log("Approve success:", response.getMessage());
    fetchBookTransactions();
    //});
  };

  const handleReturn = (row) => {
    // client.reject(request, {}, (err, response) => {
    //   if (err) {
    //     console.error("gRPC error:", err);
    //     return;
    //   }
      // console.log("Reject success:", response.getMessage());
      fetchBookTransactions();
    // });
  };

  const columnHelper = createColumnHelper();
  const columns = [
    columnHelper.accessor('book_name', { header: 'Book Name' }),
    columnHelper.accessor('is_book_available', { header: 'Is Book Available' }),
    columnHelper.accessor('member_name', { header: 'Member Name' }),
    columnHelper.accessor('borrowed_time', { header: 'Borrowed Time' }),
    columnHelper.accessor('returned_time', { header: 'Returned Time' }),
    columnHelper.display({
      id: "actions",
      header: "Actions",
      cell: ({ row }) => (
        <>
          <button type="submit" disabled={row.is_book_available !== "False"} onClick={() => handleBorrow(row)}>Borrow</button>
          <button type="submit" disabled={row.is_book_available !== "True"} onClick={() => handleReturn(row)}>Return</button>
        </>
      )
    }),
  ];

  const [pagination, setPagination] = useState({
    pageIndex: 0, // initial page index
    pageSize: 5, // default page size
  });

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(), // Enable client-side pagination
    onPaginationChange: setPagination, // update the pagination state
    state: {
      pagination,
    },
  });
  return (
    <div style={{
        display: 'flex',       // Enables flexbox layout
        justifyContent: 'center', // Centers children horizontally
        // Optional: you can add other styles like a border to see the container
        // border: '1px solid black',
        width: '100%',
      }}>
      <div>
        <h2>List Book Transaction</h2>
      <table> 
        <thead>
          {table.getHeaderGroups().map(headerGroup => (
            <tr key={headerGroup.id}>
              {headerGroup.headers.map(header => (
                <th key={header.id}>
                  {header.isPlaceholder
                    ? null
                    : flexRender(
                        header.column.columnDef.header,
                        header.getContext()
                      )}
                </th>
              ))}
            </tr>
          ))}
        </thead>

        <tbody>
          {table.getRowModel().rows.map(row => (
            <tr key={row.id}>
              {row.getVisibleCells().map(cell => (
                <td key={cell.id}>
                  {flexRender(
                    cell.column.columnDef.cell,
                    cell.getContext()
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>

      {/* Pagination UI */}
      <div style={{ marginTop: 12 }}>
        <button
          onClick={() => table.setPageIndex(0)}
          disabled={pagination.pageIndex === 0}
        >
          First
        </button>

        <button
          onClick={() => table.previousPage()}
          disabled={pagination.pageIndex === 0}
        >
          Prev
        </button>

        <span style={{ margin: '0 8px' }}>
          Page {pagination.pageIndex + 1}
        </span>

        <button onClick={() => table.nextPage()}>
          Next
        </button>

        <select
          value={pagination.pageSize}
          onChange={e =>
            table.setPageSize(Number(e.target.value))
          }
          style={{ marginLeft: 10 }}
        >
          {[5, 10, 20].map(size => (
            <option key={size} value={size}>
              Show {size}
            </option>
          ))}
        </select>
      </div>
    </div>
    </div>
  );
}

export default ListBookTransaction;