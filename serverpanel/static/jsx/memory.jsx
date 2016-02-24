import React from 'react';
import ReactDOM from 'react-dom';

import ProgressBar from './progressbar.jsx';
import TimedComponent from './timed_component.jsx';

class Memory extends TimedComponent {
    render() {

     return (<div><h3>Memory</h3>
            <ProgressBar used={ this.state.data.used } total={ this.state.data.total } free={ this.state.data.free } percent={ this.state.data.percent } />
    </div>
     );

    }
  };


ReactDOM.render(
  <Memory url={document.getElementById('memory').getAttribute('url')} pollInterval={5000} />,
  document.getElementById('memory')
);