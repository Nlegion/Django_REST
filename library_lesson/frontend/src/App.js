import React from "react";
import logo from './logo.svg';
import './App.css';
import AuthorList from "./components/Authors";
import BookList from "./components/Book";
import AuthorPage from "./components/AuthorPage";
import axios from 'axios';
import {HashRouter, Route, Redirect, Switch, Link} from "react-router-dom";

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
        const author1 = {id: 1, name: 'Грин', birthday_year: 1880}
        const author2 = {id: 2, name: 'Пушкин', birthday_year: 1799}
        const authors = [author1, author2]
        const book1 = {id: 1, name: 'Алые паруса', author: author1}
        const book2 = {id: 2, name: 'Золотая цепь', author: author1}
        const book3 = {id: 3, name: 'Пиковая дама', author: author2}
        const book4 = {id: 4, name: 'Руслан и Людмила', author: author2}
        const books = [book1, book2, book3, book4]
        this.state = {
            'authors': authors,
            'books': books
        }
        // this.state = {
        //     'authors': [],
        //     'books': []
        // }
    }

    componentDidMount() {
        //     axios
        //         .get('http://127.0.0.1:8000/api/authors/')
        //         .then(response => {
        //             const authors = response.data
        //             this.setState(
        //                 {
        //                     'authors': authors
        //                 }
        //             )
        //         }).catch(error => console.log(error))

        //#################################################

        // const authors = [{
        //     'first_name': 'Фёдор',
        //     'last_name': 'Достоевский',
        //     'birthday_year': 1821
        // },
        //     {
        //         'first_name': 'Александр',
        //         'last_name': 'Грин',
        //         'birthday_year': 1880
        //     },]
        // this.setState({
        //     'authors': authors,
        // });


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
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList books={this.state.books}/>}/>
                        <Route exact path='/author/:id' component={() => <AuthorPage authors={this.state.authors}/>}/>
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                        {/*<Redirect from='/' to '/authors' /> */}
                    </Switch>
                </HashRouter>
            </div>
        )
    }
}


export default App;
