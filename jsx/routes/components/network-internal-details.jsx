import React from 'react';

import TimedComponent from './timed_component.jsx';


class NetworkInternalDetails extends TimedComponent{
    render() {
     return (<div>{ this.state.data.map(function(network, i) {
        if (network.io.bytes_sent > 0) {
            return <div key={i}>
            <h2>{ network.device }: <small>{network.address}</small></h2>
            <p><strong>Total Traffic:</strong> { ((network.io.bytes_sent + network.io.bytes_recv)/(1024*1024*1024)).toFixed(2) } Gb
            <span className="text-muted"> (<strong>up:</strong> { (network.io.bytes_sent/(1024*1024*1024)).toFixed(2) } Gb,
            <strong> down</strong>: { (network.io.bytes_recv/(1024*1024*1024)).toFixed(2) } Gb)</span></p>
            </div>
        }
      })
      }
     </div>);
    }
  }

export default NetworkInternalDetails;