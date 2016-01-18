      var Processes = React.createClass({
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
      });


    ReactDOM.render(
      <Processes url={document.getElementById('processes').getAttribute('url')} pollInterval={5000} />,
      document.getElementById('processes')
    );