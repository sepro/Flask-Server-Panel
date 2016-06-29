import React from 'react';
import axios from 'axios';


class TimedComponent extends React.Component{
    constructor(props) {
       super(props);
       this.state = {data: []};
    }

    loadFromServer() {
        axios.get(this.props.url)
            .then((response) => {
                this.setState({data: response.data});
            })
            .catch((err) => {
                console.error(err);
            })
    }

    componentDidMount() {
        this.loadFromServer();
        this.interval = setInterval(this.loadFromServer.bind(this), this.props.pollInterval);
    }

    componentWillUnmount() {
      clearInterval(this.interval);
    }
  }

export default TimedComponent;