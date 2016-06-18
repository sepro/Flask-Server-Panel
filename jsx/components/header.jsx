import React from 'react';
import { Link } from 'react-router';


class Header extends React.Component{

    render() {
       return (
           <div>
               <p>Header</p><Link to="/">Panel</Link><Link to="/network/">Network details</Link>
           </div>
       );
    }

}

export default Header;