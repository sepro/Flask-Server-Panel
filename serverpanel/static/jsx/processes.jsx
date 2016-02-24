import TimedComponent from './timed_component.jsx';
import React from 'react';
import ReactDOM from 'react-dom';

class Processes extends TimedComponent{
        render() {

         return (<div><h3>Processes <small>(Top 5)</small></h3>
         <table className="table table-striped">
         <thead>
         <tr>
         <th>PID</th><th>Name</th><th>CPU %</th></tr></thead>
         <tbody>
         {this.state.data.slice(0,5).map(function(process ,i){
            return <tr key={i}><td>{process.pid}</td><td>{process.name}</td><td>{process.cpu_percentage}</td></tr>;
          })}
          </tbody>
        </table>
        </div>
         );

        }
      }


    ReactDOM.render(
      <Processes url={document.getElementById('processes').getAttribute('url')} pollInterval={5000} />,
      document.getElementById('processes')
    );