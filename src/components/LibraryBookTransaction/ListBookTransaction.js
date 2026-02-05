import { useState } from 'react';
import '../../App.css';
import {
  useReactTable,
  getCoreRowModel,
  getPaginationRowModel, // Import the pagination model
  flexRender,
  createColumnHelper,
} from '@tanstack/react-table';


// ... define your data and columns ...
const columnHelper = createColumnHelper();
const defaultData = [
  { book: "Book1", author: "author1", borrowed: new Date().toDateString(), returned: new Date().toDateString()}, 
  { book: "Book2", author: "author1", borrowed: new Date().toDateString(), returned: new Date().toDateString()},
  { book: "Book3", author: "author1", borrowed: new Date().toDateString(), returned: new Date().toDateString()},
  { book: "Book4", author: "author1", borrowed: new Date().toDateString(), returned: new Date().toDateString()}, 
  { book: "Book5", author: "author1", borrowed: new Date().toDateString(), returned: new Date().toDateString()},
  { book: "Book6", author: "author1", borrowed: new Date().toDateString(), returned: new Date().toDateString()},];
const columns = [
  columnHelper.accessor('book', { header: 'Book' }),
  columnHelper.accessor('author', { header: 'Author' }),
  columnHelper.accessor('borrowed', { header: 'Borrowed' }),
  columnHelper.accessor('returned', { header: 'Returned' }),
];

function ListBookTransaction() {

  const [data] = useState(() => [...defaultData]);
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
                  {cell.getValue()}
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