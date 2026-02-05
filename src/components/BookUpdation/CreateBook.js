// import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { grpcBookCreate } from '../../services/grpcWeb/ReactClient'


function CreateBook() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const onSubmit = async (data) => {

    console.log(grpcBookCreate(data.name,data.author)); // 'data' contains the form inputs
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <h2> Create Book</h2>
      <div className="form-row">
        <label htmlFor="name" className="form-label">Name:</label>
        <input className="form-input"
          id="name"
          {...register('name', { required: 'Name is required' })}
        />
        {errors.name && <p style={{ color: 'red' }}>{errors.name.message}</p>}
      </div>

      <div className="form-row">
        <label htmlFor="author"className="form-label">Author:</label>
        <input className="form-input"
          id="author"
          type="author"
          {...register('author', { required: 'Author is required' })}
        />
        {errors.author && <p style={{ color: 'red' }}>{errors.author.message}</p>}
      </div>
      <button type="submit">Create Book</button>
    </form>
  );

}
export default CreateBook;