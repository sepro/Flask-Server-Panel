import React from 'react';
import { render } from 'react-dom';

import Header from './components/header.jsx';
import Footer from './components/footer.jsx';

import Panel from './routes/panel.jsx';

class Main extends React.Component{

    render() {
       return (
           <div>
               <Header />

               {React.cloneElement(this.props.children, this.props)}

               <Footer />
           </div>
       );
    }

}

render(
  <Main url={document.getElementById('panel').getAttribute('url')}><Panel /></Main>,
  document.getElementById('panel')
);