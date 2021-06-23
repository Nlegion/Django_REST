import React from 'react'


class TODOForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            project: props.projects[0].id,
            title: '',
            text: '',
            user: props.users[0].id,
        }
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit(event) {
        this.props.createTODO(this.state.project, this.state.title, this.state.text, this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form className='form' onSubmit={(event) => this.handleSubmit(event)}>
                <div>
                    <label for='project'>Project</label>
                    <select className='select' type='select' name='project' value={this.state.project}
                            onChange={(event) => this.handleChange(event)}>{this.props.projects.map((project) =>
                        <option value={project.id}>{project.name}</option>)}
                    </select>
                </div>
                <div>
                    <label for='title'>Title</label>
                    <input type='text' name='title' value={this.state.title}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div>
                    <label for='text'>Text</label>
                    <textarea className='form-textarea' title='text' name='text' value={this.state.text}
                              onChange={(event) => this.handleChange(event)}/>
                </div>
                <div>
                    <label for='user'>User</label>
                    <select className='select' type='select' name='user' value={this.state.user}
                            onChange={(event) => this.handleChange(event)}>{this.props.users.map((user) =>
                        <option value={user.id}>{user.username}</option>)}
                    </select>
                </div>
                <div>
                    <input className='submit' type='submit' value='save'/>
                </div>
            </form>
        );
    }
}

export default TODOForm 