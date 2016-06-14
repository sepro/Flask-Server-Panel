import React from 'react';
import ReactDOM from 'react-dom';

import Hostname from './hostname.jsx';
import Uptime from './uptime.jsx';
import Memory from './memory.jsx';
import Swap from './swap.jsx';
import Disk from './disk.jsx';
import Processes from './processes.jsx'
import Pihole from './pihole.jsx'
import NetworkExternal from './network-external.jsx'
import NetworkInternal from './network-internal.jsx'

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
          <NetworkExternal url={ this.state.data.network.external } pollInterval={50000}/>
          <NetworkInternal url={ this.state.data.network.io } pollInterval={50000}/>
          <Memory url={ this.state.data.system.memory} pollInterval={10000}/>
          <Swap url={ this.state.data.system.swap} pollInterval={10000}/>
          <Disk url={ this.state.data.system.disk_space} pollInterval={10000}/>
          <Processes url={ this.state.data.system.processes} pollInterval={10000}/>
          <Pihole url={ this.state.data.pihole.stats} pollInterval={20000}/>
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