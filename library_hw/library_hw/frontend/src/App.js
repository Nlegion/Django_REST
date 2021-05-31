import React from "react";
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users";
import ProjectList from "./components/Project";
import TodoPage from "./components/TodoPage";
import axios from 'axios';
import {HashRouter, Route, Redirect, Switch, Link} from "react-router-dom";


class App extends React.Component {
    constructor(props) {

        // super(props);
        // const user1 = {email: 1, name: 'Грин', birthday_year: 1880}
        // const user2 = {email: 2, name: 'Пушкин', birthday_year: 1799}
        // const users = [user1, user2]
        //
        // const project1 = {id: 1, title: 'Алые паруса', user: 'user1', link: 'https://www.gazeta.ru/'}
        // const project2 = {id: 2, title: 'Пиковая дама', user: 'user2', link: 'https://www.gazeta.ru/'}
        // const projects = [project1, project2]
        //
        // const todo1 = {
        //     id: 1,
        //     text_fields: 'Алые паруса',
        //     created: '2021-05-30T16:49:41.828363+03:00',
        //     updated: '2021-05-30T16:49:41.828410+03:00',
        //     is_active: true,
        //     project: 1,
        //     author: 1
        // }
        // const todo2 = {
        //     id: 2, text_fields: 'тест 2',
        //     created: '2021-05-30T16:49:52.215709+03:00',
        //     updated: '2021-05-30T16:49:52.215837+03:00',
        //     is_active: false,
        //     project: 2,
        //     author: 1
        // }
        // const todos = {todo1, todo2}
        //
        // this.state = {
        //     'users': users,
        //     'projects': projects,
        //     'todos': todos,
        // }

        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/filters/title/')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))

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

    // render() {
    //     return (
    //
    //         <div>
    //             <div className="menu">Menu</div>
    //             <div><UserList users={this.state.users}/></div>
    //             <div className="footer">Footer</div>
    //         </div>
    //     )
    // }


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
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo/:id' component={() => <TodoPage todos={this.state.todos}/>}/>
                        <Redirect from='/users' to='/'/>

                        {/*<Redirect from='/' to '/authors' /> */}
                    </Switch>
                </HashRouter>
            </div>
        )
    }


}


export default App;
