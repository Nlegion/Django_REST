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
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}
export default UserList;