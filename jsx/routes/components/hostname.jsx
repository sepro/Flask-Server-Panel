import React from 'react';
import axios from 'axios';

class Hostname extends React.Component{
    constructor(props) {
       super(props);
       this.state = {data: []};
    }

    loadFromServer() {
        axios.get(this.props.url).then((response) => {
            this.setState({data: response.data});
        })
    }

    componentDidMount() {
        this.loadFromServer();
    }

    render() {
      return (<div>Hostname : <strong>{ this.state.data.hostname }</strong></div>);
    }
}

export default Hostname;