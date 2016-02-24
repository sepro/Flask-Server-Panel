import React from 'react';
import ReactDOM from 'react-dom';

class Memory extends React.Component {
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

     return (<div><h3>Memory</h3>
     <div className="progress">
        <div className="progress-bar" role="progressbar" aria-valuenow="{ (this.state.data.percent*1).toFixed(0) }" aria-valuemin="0" aria-valuemax="100" style={{width: (this.state.data.percent*1).toFixed(0) + '%'}}>
        <span className="progress-label">Used { (this.state.data.used/1073741824).toFixed(2) } / { (this.state.data.total/1073741824).toFixed(2) } Gb <span className="text-muted">(Available: { (this.state.data.available/1073741824).toFixed(2) } Gb)</span></span>
        </div>
    </div>
    </div>
     );

    }
  };


ReactDOM.render(
  <Memory url={document.getElementById('memory').getAttribute('url')} pollInterval={5000} />,
  document.getElementById('memory')
);