import React from 'react';

import Logo from './components/logo.jsx';
import Hostname from './components/hostname.jsx';
import Uptime from './components/uptime.jsx';
import Memory from './components/memory.jsx';
import Swap from './components/swap.jsx';
import Disk from './components/disk.jsx';
import Processes from './components/processes.jsx'
import Pihole from './components/pihole.jsx'
import NetworkExternal from './components/network-external.jsx'
import NetworkInternal from './components/network-internal.jsx'


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
          <div className="row">
              <div className="col-lg-3">
                  <Logo url={ this.state.data.system.temp }  pollInterval={1000}/>
              </div>
              <div className="col-lg-9">
                  <Hostname url={ this.state.data.server.hostname } />
                  <Uptime url={ this.state.data.server.uptime } pollInterval={1000}/>
                  <NetworkExternal url={ this.state.data.network.external } pollInterval={50000}/>
                  <NetworkInternal url={ this.state.data.network.io } pollInterval={50000}/>
              </div>
          </div>
          <hr />
          <Memory url={ this.state.data.system.memory} pollInterval={10000}/>
          <Swap url={ this.state.data.system.swap} pollInterval={10000}/>
          <Disk url={ this.state.data.system.disk_space} pollInterval={10000}/>
          <hr />
          <Processes url={ this.state.data.system.processes} pollInterval={10000}/>
          <hr />
          <Pihole url={ this.state.data.pihole.stats} pollInterval={20000}/>
          </div>
          );
      } else {
          return (<div></div>);
      }
    }
}

export default Panel;