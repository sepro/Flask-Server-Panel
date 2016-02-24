import React from 'react';
import ReactDOM from 'react-dom';

class Hostname extends React.Component{
    loadFromServer: function() {
        $.ajax({
          url: this.props.url,
          dataType: 'json',
          cache: false,
          success: function(data) {
            this.setState({data: data});
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(this.props.url, status, err.toString());
          }.bind(this)
        });
      },
    getInitialState: function() {
        return {data: []};
    },
    componentDidMount: function() {
        this.loadFromServer();
    },
    render: function() {

     return (<span>hostname : <strong>{ this.state.data.hostname }</strong></span>);

    }
}

ReactDOM.render(
  <Hostname url={document.getElementById('hostname').getAttribute('url')} />,
  document.getElementById('hostname')
);