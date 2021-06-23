import React from 'react'
import {Link} from "react-router-dom";

class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            title: '',
            id: '',
            users: props.users[0].id
        }
    }

    handleChange(event) {
        this.setState({[event.target.title]: event.target.value});
    }

    handleSubmit(event) {
        this.props.createProject(this.state.title, this.state.id, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form className='form' onSubmit={(event) => this.handleSubmit(event)}>
                <div>
                    <label for='title'>title</label>
                    <input type='text' name='title' value={this.state.title}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div>
                    <label for='id'>id</label>
                    <input type='text' name='id' value={this.state.id}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div>
                    <label for='users'>Users</label>
                    <select multiple className='select' type='select' name='users' value={this.state.users}
                            onChange={(event) => this.handleChange(event)}>{this.props.users.map((users) =>
                        <option value={users.id}>{users.username}</option>)}
                    </select>
                </div>
                <div>
                    <input className='submit' type='submit' value='save'/>
                </div>
            </form>
        );
    }
}

export default ProjectForm