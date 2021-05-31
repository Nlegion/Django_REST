import React from 'react'
import {useParams} from 'react-router-dom';

const TodoPage = ({todos}) => {

    let {id} = useParams();
    let todo = todos.find((todo) => todo.project == id);

    return (
        <div>
            {todo.text_fields}
            {todo.created}
            {todo.updated}
            {todo.author}
            {todo.is_active}
        </div>
    )
}

export default TodoPage;
