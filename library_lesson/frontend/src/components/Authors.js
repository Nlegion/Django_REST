import React from 'react'
import {Link} from "react-router-dom";

const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.id}
            </td>
            <td>
                <Link to={`/author/${author.id}`}>{author.first_name}</Link>
            </td>
            <td>
                <Link to={`/author/${author.id}`}>{author.last_name}</Link>
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}


const AuthorList = ({authors}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Имя
            </th>
            <th>
                Фамилия
            </th>
            <th>
                Дата Рождения
            </th>
            {authors.map((author) => <AuthorItem author={author}/>)}
        </table>
    )
}
export default AuthorList;