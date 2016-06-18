import React from 'react';

import TimedComponent from './timed_component.jsx';


class NetworkInternal extends TimedComponent{
    render() {
     return (<div>Local IP : <ul>{ this.state.data.map(function(network, i) {
        if (network.io.bytes_sent > 0) {
            return <li key={i}>{ network.device }: {network.address}</li>
        }
      })
      }</ul>
     </div>);
    }
  }

export default NetworkInternal;