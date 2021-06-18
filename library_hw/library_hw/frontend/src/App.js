import React from "react";
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users";
import ProjectList from "./components/Project";
import TODOList from "./components/TodoPage";
import LoginForm from "./components/Auth";
import axios from 'axios';
import {HashRouter, Route, Redirect, Switch, Link} from "react-router-dom";
import TODOForm from "./components/TodoForm";
import ProjectForm from "./components/ProjectForm";

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

    createProject(title, id, users) {
        let headers = this.get_headers()
        const data = {name: title, repo: id, users: users}
        axios.post(`http://localhost:8080/api/projects/`, data, {headers}).then(response => {
            let new_project = response.data
            const users = this.state.users.filter((users) => users.id === new_project.users)[0]
            new_project.users = users
            this.setState({projects: [...this.state.projects, new_project]})
        }).catch(error => console.log(error))
    }

    deleteProject(id) {
        let headers = this.get_headers()
        axios.delete(`http://localhost:8080/api/projects/${id}/`, {headers}).then(response => {
            this.setState({projects: this.state.projects.filter((project) => project.id !== id)})
        }).catch(error => console.log(error))
    }

    createTODO(project, title, text_fields, users) {
        let headers = this.get_headers()
        const data = {project: project, text_fields: text_fields, users: users}
        axios.post(`http://localhost:8080/api/TODO/`, data, {headers}).then(response => {
            let n_todo = response.data
            const project = this.state.projects.filter((project) => project.id === n_todo.project)[0]
            const users = this.state.users.filter((users) => users.id === n_todo.users)[0]
            n_todo.project = project
            n_todo.users = users
            this.setState({todos: [...this.state.todos, n_todo]})
        }).catch(error => console.log(error))
    }

    deleteTODO(id) {
        let headers = this.get_headers()
        axios.delete(`http://localhost:8080/api/TODO/${id}/`, {headers}).then(response => {
            this.setState({todos: this.state.todo.filter((todo) => todo.id !== id)})
        }).catch(error => console.log(error))
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

                        {/*<Route exact path='/todo/:id' component={() => <TodoPage todos={this.state.todos}/>}/>*/}
                        <Redirect from='/users' to='/'/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>}/>
                        <Route exact path='/user/:id' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}
                                                                                    editProject={(id) => this.editProject(id)}
                                                                                    deleteProject={(id) => this.deleteProject(id)}/>}/>
                        <Route exact path='/projects/create'
                               component={() => <ProjectForm
                                   users={this.state.users} createProject={(title, id, users) =>
                                   this.createProject(title, id, users)}/>}/>
                        <Route exact path='/todos/create'
                               component={() => <TODOForm projects={this.state.projects} users={this.state.users}
                                                          createTODO={(project, text_fields, users) =>
                                                              this.createTODO(project, text_fields, users)}/>}/>
                        <Route exact path='/todos'
                               component={() => <TODOList todos={this.state.todos}
                                                          editToDo={(id) => this.editToDo(id)}
                                                          deleteToDo={(id) => this.deleteToDo(id)}/>}/>

                    </Switch>
                </HashRouter>
            </div>
        )
    }


}


export default App;
