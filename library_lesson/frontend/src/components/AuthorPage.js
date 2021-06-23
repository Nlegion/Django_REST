import React from 'react'
import {useParams} from 'react-router-dom';

const AuthorPage = ({authors}) => {

    let {id} = useParams();
    let author = authors.find((author) => author.id == id);

    return (
        <div>
            {author.name}
            {author.birthday_year}
        </div>
    )
}

export default AuthorPage;