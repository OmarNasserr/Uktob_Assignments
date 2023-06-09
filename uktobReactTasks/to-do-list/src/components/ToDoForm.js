import { useState } from "react";

function ToDoForm({ addTodo }) {

    const [value,setValue] = useState("");

    const handleInputChange = (e) => {
        setValue(e.target.value);
      };


    const handleSubmit = (e) => {
        e.preventDefault();
        addTodo(value);
        setValue("");
    };

    return(
        <>
            <form className="ToDoForm" onSubmit={handleSubmit}>
                <input type="text" className="form-control"
                 placeholder="What Is The Task Today?"
                 value={value}
                 onChange={handleInputChange} />
                <button type="submit" className="btn btn-secondary">Submit</button>
            </form>
        </>
    )
}

export default ToDoForm;