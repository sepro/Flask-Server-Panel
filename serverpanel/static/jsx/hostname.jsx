import React from 'react';
import ReactDOM from 'react-dom';

class Hostname extends React.Component{
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
    }

    render() {
      return (<span>hostname : <strong>{ this.state.data.hostname }</strong></span>);
    }
}

ReactDOM.render(
  <Hostname url={document.getElementById('hostname').getAttribute('url')} />,
  document.getElementById('hostname')
);