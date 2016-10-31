import React from 'react';
import axios from 'axios';

import NetworkInternalDetails from './components/network-internal-details.jsx';
import Hostname from './components/hostname.jsx';

class Network extends React.Component{
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
                       <h1>Local</h1>
                       <hr />
                       <NetworkInternalDetails url={ this.state.data.network.io } pollInterval={50000}/>
                   </div>
               );
          } else {
                return (<div></div>)
          }
    }

}

export default Network;