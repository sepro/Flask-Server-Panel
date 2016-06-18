import React from 'react';

import TimedComponent from './timed_component.jsx';


class Uptime extends TimedComponent{
    render() {
     return (<div>uptime : <strong>{ this.state.data.uptime }</strong></div>);
    }
  }

export default Uptime;