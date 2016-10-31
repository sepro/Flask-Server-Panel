import React from 'react';

import TimedComponent from './timed_component.jsx';


class Temperature extends TimedComponent{
    render() {
     return (<div>CPU Temp : <strong>{ typeof(this.state.data.cpu) != "undefined" ? this.state.data.cpu.toFixed(1) : 0 } °C</strong></div>);
    }
  }

export default Temperature;