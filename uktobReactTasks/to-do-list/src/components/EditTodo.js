import { useState } from "react";

function EditTodo({ editTodo , task }) {

    const [value,setValue] = useState(task.task);

    const handleInputChange = (e) => {
        setValue(e.target.value);
      };


    const handleSubmit = (e) => {
        e.preventDefault();
        editTodo(value, task.id);
        setValue("");
    };

    return(
        <>
            <form className="ToDoForm" onSubmit={handleSubmit}>
                {/* <h1>Get Things Done</h1> */}
                <input type="text" className="form-control"
                 placeholder="Update Task?"
                 value={value}
                 onChange={handleInputChange} />
                <button type="submit" className="btn btn-secondary">Submit</button>
            </form>
        </>
    )
}

export default EditTodo;