import React from 'react';
import ReactDOM from 'react-dom';

import ProgressBar from './progressbar.jsx';
import TimedComponent from './timed_component.jsx';

class Disk extends TimedComponent {
        render() {

         return (<div><h3>Disk</h3>
         {this.state.data.map(function(disk ,i){
            return          <div key={i}><strong>{ disk.mountpoint }</strong>
                <ProgressBar used={ disk.usage.used } total={ disk.usage.total } free={ disk.usage.free } percent={ disk.usage.percent } />
            </div>;
          })}

        </div>
         );

        }
      }


export default Disk;