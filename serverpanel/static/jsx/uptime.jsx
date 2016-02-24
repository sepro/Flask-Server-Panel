import React from 'react';
import ReactDOM from 'react-dom';

class Uptime extends React.Component{
    constructor(props) {
       super(props);
       this.state = {data: []};
    }

    loadFromServer() {
        $.ajax({
          url: this.props.url,
          dataType: 'json',
          success: (data) => {
            this.setState({data: data});
          },
          error: (xhr, status, err) => {
            console.error(this.props.url, status, err.toString());
          }
        });
    }

    componentDidMount() {
        this.loadFromServer();
        setInterval(this.loadFromServer.bind(this), this.props.pollInterval);
    }

    render() {
     return (<span>uptime : <strong>{ this.state.data.uptime }</strong></span>);
    }
  }

ReactDOM.render(
  <Uptime url={document.getElementById('uptime').getAttribute('url')} pollInterval={1000} />,
  document.getElementById('uptime')
);