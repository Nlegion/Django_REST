import React from 'react';
import './App.css';
import AuthorList from "./components/Author";
import AuthorPage from './components/AuthorPage.js';
import BookList from './components/Book.js';
import LoginForm from './components/Auth.js';
import BookForm from './components/BookForm.js';
import axios from 'axios';
import {HashRouter, Route, Redirect, Switch, Link} from 'react-router-dom';

const NotFound404 = ({location}) => {
    return (
        <div>
            Not found: {location.pathname}
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'books': [],
            'token': ''
        }
    }

    restore_token() {
        let token = localStorage.getItem('token');
        this.setState(
            {
                'token': token
            }, this.load_data
        );
    }

    create_header() {
        if (!this.is_auth())
            return {};

        return {
            'Authorization': 'Token ' + this.state.token
        }
    }

    load_data() {
        let headers = this.create_header();

        axios
            .get('http://127.0.0.1:8000/api/authors/', {headers})
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/api/books/', {headers})
            .then(response => {
                const books = response.data
                this.setState(
                    {
                        'books': books
                    }
                )
            })
            .catch(error => {
                this.setState(
                    {
                        'books': []
                    }
                )
                console.log(error)
            })
    }

    componentDidMount() {
        this.restore_token();
    }

    is_auth() {
        return !!(this.state.token);
    }

    logout() {
        localStorage.removeItem('token')
        this.setState(
            {
                'token': ''
            }, this.load_data
        );
    }

    get_token(login, password) {
        axios
            .post(
                'http://127.0.0.1:8000/api-token-auth/',
                {"username": login, "password": password}
            )
            .then(response => {
                localStorage.setItem('token', response.data.token)
                this.setState(
                    {
                        'token': response.data.token
                    }, this.load_data
                );
            })
            .catch(error => alert('Wrong password'))
    }

    delete_book(id) {
        let headers = this.create_header();
        axios
            .delete(`http://127.0.0.1:8000/api/books/${id}/`, {headers})
            .then(response => {
                this.setState(
                    {
                        'books': this.state.books.filter((book) => book.id !== id)
                    }
                )
            })
            .catch(error => {
                console.log(error)
            })
    }

    create_book(name, authors) {
        console.log("create_book " + name + " - " + authors);
        console.log(authors);

        axios
            .post(
                'http://127.0.0.1:8000/api/books/',
                {"name": name, "authors": authors}
            )
            .then(response => {
                this.load_data();
            })
            .catch(error => console.log('Wrong password'))
    }

    render() {
        return (
            <div>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                            <li>
                                <Link to='/books/create'>New book</Link>
                            </li>
                            <li>{
                                this.is_auth() ?
                                    <button onClick={() => this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>
                            }
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList books={this.state.books}
                                                                              delete_book={(id) => this.delete_book(id)}/>}/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route exact path='/books/create'
                               component={() => <BookForm
                                   create_book={(name, authors) => this.create_book(name, authors)}
                                   authors={this.state.authors}/>}/>
                        <Route exact path='/author/:id' component={() => <AuthorPage authors={this.state.authors}/>}/>
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>
        )
    }
}

export default App;