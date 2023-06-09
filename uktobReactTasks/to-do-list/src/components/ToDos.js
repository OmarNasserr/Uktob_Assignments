import { faPenToSquare, faTrash } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

function ToDos({ task, toggleComplete, deleteTodo, editTodo }) {

    return (
        <div className="toDo">
            <p onClick={() => toggleComplete(task.id)} className={`${task.completed ? 'completed' : ""}`}
                style={{ textDecoration: task.completed ? "line-through" : "none" }}
            >{task.task}</p>
            <div className="iconss">
                <FontAwesomeIcon style={{ cursor: "pointer" }} icon={faPenToSquare} onClick={() => editTodo(task.id)} />
                <FontAwesomeIcon style={{ cursor: "pointer" }} icon={faTrash} onClick={() => deleteTodo(task.id)} />
            </div>
        </div>
    )
}

export default ToDos;