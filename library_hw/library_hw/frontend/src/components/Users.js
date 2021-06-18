import React from 'react'


const UserItem = ({users}) => {
    return (
        <tr>
            <td>
                {users.email}
            </td>

            <td>
                {users.name}
            </td>
        </tr>

    )
}


const UserList = ({users}) => {
    return (
        <table>
            <tr>
                <td>Email</td>
                <td>Name</td>
            </tr>
            {users.map((users) => <UserItem user={users}/>)}
        </table>
    )
}
export default UserList;