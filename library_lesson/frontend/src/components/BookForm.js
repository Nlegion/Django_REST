import React from 'react'


class BookForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'name': '',
            'authors': []
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleChangeAuthors(event) {
        if (!event.target.selectedOptions) {
            return;
        }

        let authors = [];
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            authors.push(event.target.selectedOptions.item(i).value);
        }
        console.log(authors);

        this.setState(
            {
                'authors': authors
            }
        );
    }


    handleSubmit(event) {
        this.props.create_book(this.state.name, this.state.authors);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="name" placeholder="name" value={this.state.name}
                       onChange={(event) => this.handleChange(event)}/>
                <select multiple name="authors" className='form-control'
                        onChange={(event) => this.handleChangeAuthors(event)}>
                    {this.props.authors.map((item) => <option value={item.id}>{item.last_name}</option>)}
                </select>

                <input type="submit" value="Create"/>
            </form>
        );

    }
}

export default BookForm;