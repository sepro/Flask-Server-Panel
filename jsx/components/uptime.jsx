import TimedComponent from './timed_component.jsx';
import React from 'react';
import ReactDOM from 'react-dom';

class Uptime extends TimedComponent{
    render() {
     return (<div>uptime : <strong>{ this.state.data.uptime }</strong></div>);
    }
  }

export default Uptime;