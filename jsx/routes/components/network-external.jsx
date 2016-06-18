import React from 'react';

import TimedComponent from './timed_component.jsx';


class NetworkExternal extends TimedComponent{
    render() {
     return (<div>External IP : <strong>{ this.state.data.ip }</strong> (country: { this.state.data.country })</div>);
    }
  }

export default NetworkExternal;
