import React from 'react'
import {useParams} from 'react-router-dom';
import {Link} from "react-router-dom";

const TODOItem = ({todos, deleteToDo}) => {

    let {id} = useParams();
    let todo = todos.find((todo) => todo.project == id);

    return (
        <tr>
            <td>{todo.text_fields}</td>
            <td>{todo.author}</td>
            <td>{todo.updated}</td>
            <td>
                <button onClick={() => deleteToDo(todo.id)} type='submit'>Delete</button>
            </td>
        </tr>

    )
}

const TODOList = ({todos, deleteTODO}) => {
    return (<div>
            <nav className='menu'>
                <Link className='menu-link' to='/TODO/create/'>Create TODO</Link>
            </nav>
            <table className='table'>
                <thead>
                <tr>
                    <th>Aктивность</th>
                    <th>Проект</th>
                    <th>Заголовок</th>
                    <th>Пользователь</th>
                    <th>Создана</th>
                    <th>Обновлена</th>
                    <th> </th>
                </tr>
                </thead>
                {todos.map((todo) => <TODOItem todo={todo} deleteTODO={deleteTODO}/>)}
            </table>
        </div>
    )
}


export default TODOList;
