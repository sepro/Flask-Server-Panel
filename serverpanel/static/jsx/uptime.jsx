import TimedComponent from './timed_component.jsx';
import React from 'react';
import ReactDOM from 'react-dom';

class Uptime extends TimedComponent{
    render() {
     return (<span>uptime : <strong>{ this.state.data.uptime }</strong></span>);
    }
  }

ReactDOM.render(
  <Uptime url={document.getElementById('uptime').getAttribute('url')} pollInterval={1000} />,
  document.getElementById('uptime')
);