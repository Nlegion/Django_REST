import React from 'react'


const UserItem = ({user}) => {
    return (

        <tr>
            <td>
                {user.email}
            </td>

            <td>
                {user.name}
            </td>
            <td>
                {user.birthday_year}
            </td>
        </tr>

    )
}


const UserList = ({users}) => {
    return (
        <table>
            <th>
                Email
            </th>
            <th>
                Имя пользователя
            </th>
            <th>
                Дата рождения
            </th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}
export default UserList;