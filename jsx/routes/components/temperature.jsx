import React from 'react';

import TimedComponent from './timed_component.jsx';


class Temperature extends TimedComponent{
    render() {
     return (<div>CPU Temp : <strong>{ this.state.data.cpu } °C</strong></div>);
    }
  }

export default Temperature;