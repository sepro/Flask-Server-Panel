      var Swap = React.createClass({
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

         return (<div><h3>Swap</h3>
         <div className="progress">
            <div className="progress-bar" role="progressbar" aria-valuenow="{ (this.state.data.percent*1).toFixed(0) }" aria-valuemin="0" aria-valuemax="100" style={{width: (this.state.data.percent*1).toFixed(0) + '%'}}>
            <span className="progress-label">Used { (this.state.data.used/1024**3).toFixed(2) } / { (this.state.data.total/1024**3).toFixed(2) } Gb <span className="text-muted">(Free: { (this.state.data.free/1024**3).toFixed(2) } Gb)</span></span>
            </div>
        </div>
        </div>
         );

        }
      });


    ReactDOM.render(
      <Swap url={document.getElementById('swap').getAttribute('url')} pollInterval={5000} />,
      document.getElementById('swap')
    );