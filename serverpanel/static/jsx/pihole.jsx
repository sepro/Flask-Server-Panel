      var Pihole = React.createClass({
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
            if (this.state.data.enabled) {
              return (<div><h3>Pi-Hole</h3>
              <div className="row">
                 <div className="col-lg-3 col-xs-6 text-center">
                 <h4>{ this.state.data.dns_queries_today }</h4>
                 <p>DNS queries today</p>
                 </div>
                 <div className="col-lg-3 col-xs-6  text-center">
                 <h4>{ this.state.data.ads_blocked_today }</h4>
                 <p>Ads blocked today</p>
                 </div>
                 <div className="col-lg-3 col-xs-6  text-center">
                 <h4>{ this.state.data.ads_percentage_today.toFixed(2) } %</h4>
                 <p>Percentage blocked</p>
                 </div>
                 <div className="col-lg-3 col-xs-6  text-center">
                 <h4>{ this.state.data.blocked_domains }</h4>
                 <p>Blocked domains</p>
                 </div>
              </div>
                 </div>);
                } else {
                    return (<div></div>);
                }

        }
      });


    ReactDOM.render(
      <Pihole url={document.getElementById('pihole').getAttribute('url')} pollInterval={10000} />,
      document.getElementById('pihole')
    );