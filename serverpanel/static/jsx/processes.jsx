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

         return (<div><h3>Processes</h3>
         {this.state.data.map(function(process ,i){
            return <div key={i}>{process.pid}, {process.name}, {process.cpu_percentage}</div>;
          })}

        </div>
         );

        }
      });


    ReactDOM.render(
      <Processes url={document.getElementById('processes').getAttribute('url')} pollInterval={5000} />,
      document.getElementById('processes')
    );