import React from 'react';
import ReactDOM from 'react-dom';

import Hostname from './hostname.jsx';
import Uptime from './uptime.jsx';
import Memory from './memory.jsx';

class Panel extends React.Component{
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
      if (this.state.data.server) {
          return (
          <div>
          <Hostname url={ this.state.data.server.hostname } />
          <Uptime url={ this.state.data.server.uptime } pollInterval={1000}/>
          <Memory url={ this.state.data.system.memory} pollInterval={10000}/>
          </div>
          );
      } else {
          return (<div></div>);
      }
    }
}

ReactDOM.render(
  <Panel url={document.getElementById('panel').getAttribute('url')} />,
  document.getElementById('panel')
);