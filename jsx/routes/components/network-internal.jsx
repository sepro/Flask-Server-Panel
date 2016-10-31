import React from 'react';

import TimedComponent from './timed_component.jsx';


class NetworkInternal extends TimedComponent{
    render() {
     return (<div><p>Local IP : </p><div>{ this.state.data.map(function(network, i) {
        if (network.io.bytes_sent > 0) {
            return <p key={i}>{ network.device }: {network.address}</p>
        }
      })
      }</div>
     </div>);
    }
  }

export default NetworkInternal;