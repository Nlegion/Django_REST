import React from "react";
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users";
import ProjectList from "./components/Project";
import TodoPage from "./components/TodoPage";
import LoginForm from "./components/Auth";
import axios from 'axios';
import {HashRouter, Route, Redirect, Switch, Link} from "react-router-dom";

class App extends React.Component {
    constructor(props) {
        super(props);
        let token = localStorage.getItem('token');
        this.state = {
            'users': [],
            'projects': [],
            'TODO': [],
            'token': token
        }
    }

    restore_token() {
        let token = localStorage.getItem('token');
        this.setState(
            {
                'token': token
            }
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
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/filters/title/')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/ToDo/')
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => console.log(error))
    }


    componentDidMount() {
        this.restore_token();
        this.load_data();
    }

    is_auth() {
        return !!(this.state.token != '');
    }

    logout() {
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
                this.setState(
                    {
                        'token': response.data.token
                    }, this.load_data
                );
                localStorage.setItem('token', response.data.token)
            })
            .catch(error => alert('Лажа с паролем'))
    }


    render() {
        return (
            <div>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Пользователи</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Проекты</Link>
                            </li>
                            <li>
                                <Link to='/todos'>Тудусики</Link>
                            </li>
                            <li>
                                {this.is_auth() ?
                                    <button onClick={() => this.logout()}>Логаут</button>
                                    :
                                    <Link to='/login'>Логин</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo/:id' component={() => <TodoPage todos={this.state.todos}/>}/>
                        <Redirect from='/users' to='/'/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>}/>
                        <Route exact path='/user/:id' component={() => <UserList users={this.state.users}/>}/>
                    </Switch>
                </HashRouter>
            </div>
        )
    }


}


export default App;
