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
              return (<div><h3>PiHole</h3>
                 <p>DNS queries today: { this.state.data.dns_queries_today }</p>
                 <p>Ads blocked today: { this.state.data.ads_blocked_today }</p>
                 <p>Percentage blocked: { this.state.data.ads_percentage_today }</p>
                 <p>Blocked domains: { this.state.data.blocked_domains }</p>
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