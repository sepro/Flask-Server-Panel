import React from 'react';
import { render } from 'react-dom';

import {Router, Route, IndexRoute, browserHistory} from 'react-router'

//import main components (which will appear on every page)
import Header from './components/header.jsx';
import Footer from './components/footer.jsx';

//import the routes
import Panel from './routes/panel.jsx';
import Network from './routes/network.jsx';


class Main extends React.Component{

    render() {
       return (
           <div>
               <Header />

               {React.cloneElement(this.props.children, this.props.route)}

               <Footer />
           </div>
       );
    }

}

const router = (
    <Router history={browserHistory}>
        <Route path="/" component={Main} url={document.getElementById('panel').getAttribute('url')}>
            <IndexRoute component={Panel}></IndexRoute>
            <Route path="/network/" component={Network}></Route>
        </Route>
    </Router>
);

render(
  router,
  document.getElementById('panel')
);