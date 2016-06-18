import React from 'react';

import ProgressBar from './progressbar.jsx';
import TimedComponent from './timed_component.jsx';


class Swap extends TimedComponent {
    render() {

         return (<div><h3>Swap</h3>
            <ProgressBar used={ this.state.data.used } total={ this.state.data.total } free={ this.state.data.free } percent={ this.state.data.percent } />
         </div>
         );

        }
    }

export default Swap;