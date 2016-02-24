import React from 'react';
import ReactDOM from 'react-dom';

import ProgressBar from './progressbar.jsx';

class Swap extends React.Component {
    constructor(props) {
       super(props);
       this.state = {data: []};
    }

    loadFromServer() {
        $.ajax({
          url: this.props.url,
          dataType: 'json',
          success: (data) => {
            this.setState({data: data});
          },
          error: (xhr, status, err) => {
            console.error(this.props.url, status, err.toString());
          }
        });
    }

    componentDidMount() {
        this.loadFromServer();
        setInterval(this.loadFromServer.bind(this), this.props.pollInterval);
    }

    render() {

         return (<div><h3>Swap</h3>
            <ProgressBar used={ this.state.data.used } total={ this.state.data.total } free={ this.state.data.free } percent={ this.state.data.percent } />
         </div>
         );

        }
    }


    ReactDOM.render(
      <Swap url={document.getElementById('swap').getAttribute('url')} pollInterval={5000} />,
      document.getElementById('swap')
    );