      var Disk = React.createClass({
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

         return (<div><h3>Disk</h3>
         {this.state.data.map(function(disk){
            return          <div><strong>{ disk.mountpoint }</strong><div className="progress">
            <div className="progress-bar" role="progressbar" aria-valuenow="{ (disk.usage.percent*1).toFixed(0) }" aria-valuemin="0" aria-valuemax="100" style={{width: (disk.usage.percent*1).toFixed(0) + '%'}}>
            <span className="progress-label">Used { (disk.usage.used/1024**3).toFixed(2) } / { (disk.usage.total/1024**3).toFixed(2) } Gb <span className="text-muted">(Free: { (disk.usage.free/1024**3).toFixed(2) } Gb)</span></span>
            </div>
        </div></div>;
          })}

        </div>
         );

        }
      });


    ReactDOM.render(
      <Disk url={document.getElementById('disk').getAttribute('url')} pollInterval={5000} />,
      document.getElementById('disk')
    );