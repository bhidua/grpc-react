// import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { grpcMemberUpdate } from '../../services/grpcWeb/ReactClient'


function UpdateMember() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const onSubmit = async (data) => {

    console.log(grpcMemberUpdate(data.name,data.author)); // 'data' contains the form inputs
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <h2> Update Book</h2>
      <div className="form-row">
        <label htmlFor="id" className="form-label">Id:</label>
        <input className="form-input"
          id="id"
          {...register('id', { required: 'Id is required' })}
        />
        {errors.id && <p style={{ color: 'red' }}>{errors.id.message}</p>}
      </div>
      <div className="form-row">
        <label htmlFor="name" className="form-label">Name:</label>
        <input className="form-input"
          id="name"
          {...register('name', { required: 'Name is required' })}
        />
        {errors.name && <p style={{ color: 'red' }}>{errors.name.message}</p>}
      </div>

      <div className="form-row"> 
        <label htmlFor="phone" className="form-label">Phone:</label>
        <input className="form-input"
          id="phone"
          type="phone"
          {...register('phone', { required: 'Phone is required' })}
        />
        {errors.phone && <p style={{ color: 'red' }}>{errors.phone.message}</p>}
      </div>
      <button type="submit">Update Member</button>
    </form>
  );

}
export default UpdateMember;