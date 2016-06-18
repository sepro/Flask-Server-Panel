import React from 'react';


class TimedComponent extends React.Component{
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
        this.interval = setInterval(this.loadFromServer.bind(this), this.props.pollInterval);
    }

    componentWillUnmount() {
      clearInterval(this.interval);
    }
  }

export default TimedComponent;