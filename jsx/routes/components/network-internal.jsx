import React from 'react';

import TimedComponent from './timed_component.jsx';


class NetworkInternal extends TimedComponent{
    render() {
     return (<div>Local IP : <span>{ this.state.data.map(function(network, i) {
        if (network.io.bytes_sent > 0) {
            return <span key={i}>{ network.device }: {network.address}</span>
        }
      })
      }</span>
     </div>);
    }
  }

export default NetworkInternal;