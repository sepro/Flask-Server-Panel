import React from 'react';


class ProgressBar extends React.Component {
    render() {

         return (
         <div className="progress">
            <div className="progress-bar" role="progressbar" aria-valuenow="{ (this.props.percent*1).toFixed(0) }" aria-valuemin="0" aria-valuemax="100" style={{width: (this.props.percent*1).toFixed(0) + '%'}}>
            <span className="progress-label">Used { (this.props.used/1073741824).toFixed(2) } / { (this.props.total/1073741824).toFixed(2) } Gb <span className="text-muted">(Free: { (this.props.free/1073741824).toFixed(2) } Gb)</span></span>
            </div>
        </div>
         );

        }
    }

export default ProgressBar;