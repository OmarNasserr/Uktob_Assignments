import { useState } from "react";
import ToDoForm from "./ToDoForm";
import { v4 as uuidv4 } from 'uuid';
import ToDos from "./ToDos";
import EditTodo from "./EditTodo";
// uuidv4();

function ToDo() {

    const [todos, setTodos] = useState([]);

    const addTodo = (todo) => {

        setTodos([...todos, {
            id: uuidv4(), task: todo,
            compledted: false, isEditing: false
        }]);

        console.log(todos);
    }

    const toggleComplete = (id) => {
        setTodos(
            todos.map((todo) =>
                todo.id === id ? { ...todo, completed: !todo.completed } : todo
            )
        );
    };

    const deleteTodo = (id) => {
        setTodos(todos.filter((todo) => todo.id !== id));
    };

    const editTodo = (id) => {
        setTodos(todos.map(todo => todo.id === id ? { ...todo, isEditing: !todo.isEditing } : todo))
    }

    const editTask = (task, id) => {
        setTodos(todos.map(todo => todo.id === id ? {...todo , task, isEditing: !todo.isEditing}: todo))
    }

    return (
        <>
            <div className="container  mt-5">
            <h1>Get Things Done</h1>
                <ToDoForm addTodo={addTodo} />
                {todos.map((todo, index) => (
                    todo.isEditing ? (
                        <EditTodo editTodo={editTask} task={todo} />
                    ) : (
                        <ToDos task={todo} key={index} toggleComplete={toggleComplete}
                            deleteTodo={deleteTodo} editTodo={editTodo} />
                    )
                ))}
            </div>

        </>

    );
}

export default ToDo;