import React from 'react'

const BookItem = ({book, delete_book}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors.name}
            </td>
            <td>
                <button onClick={() => delete_book(book.id)}>
                    Удалить
                </button>

            </td>
        </tr>
    )
}

const BookList = ({books, delete_book}) => {
    return (
        <table>
            <th>
                Id
            </th>
            <th>
                Название
            </th>
            <th>
                Авторы
            </th>
            <th>
                Кнопка удаления
            </th>
            {books.map((book) => <BookItem book={book} delete_book = {delete_book}/>)}
        </table>
    )
}

export default BookList;