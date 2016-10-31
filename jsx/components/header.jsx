import React from 'react';
import { Link } from 'react-router';


class Header extends React.Component{

    render() {
       return (
           <div>
               <hr />
               <ul className="nav nav-pills">
                    <li><Link to="/">Panel</Link></li>
                    <li><Link to="/network/">Network details</Link></li>
               </ul>
               <hr />
           </div>
       );
    }

}

export default Header;