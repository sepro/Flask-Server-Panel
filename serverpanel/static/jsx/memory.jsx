      var Memory = React.createClass({
        loadFromServer: function() {
            $.ajax({
              url: this.props.url,
              dataType: 'json',
              cache: false,
              success: function(data) {
                this.setState({data: data});
              }.bind(this),
              error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
              }.bind(this)
            });
          },
        getInitialState: function() {
            return {data: []};
        },
        componentDidMount: function() {
            this.loadFromServer();
            setInterval(this.loadFromServer, this.props.pollInterval);
        },
        render: function() {

         return (<div><h3>Memory</h3>
         <p>Available : <strong>{ (this.state.data.available/1024**3).toFixed(2) } Gb</strong></p>
         <p>Used : <strong>{ (this.state.data.used/1024**3).toFixed(2) } Gb</strong></p>
         <p>Total : <strong>{ (this.state.data.total/1024**3).toFixed(2) } Gb</strong></p>
         <p>Percent : <strong>{ (this.state.data.percent*1).toFixed(1) } %</strong></p></div>
         );

        }
      });


    ReactDOM.render(
      <Memory url={document.getElementById('memory').getAttribute('url')} pollInterval={5000} />,
      document.getElementById('memory')
    );