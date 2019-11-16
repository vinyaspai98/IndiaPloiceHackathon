import React, { Component } from 'react';
import SearchAppBar from './Components/appbar';
import Card from './Components/Cards/Card';
import Icons from './Components/Cards/mapIcon';
import { height } from '@material-ui/system';

class App extends Component {

//   constructor() {
//     super()
//     this.state={
//         Icons: Icons,
//     }
// }

  render(){
    return (
      <div >
        <SearchAppBar />
        <Card data={Icons} />
      </div>
    );
  }
}

export default App;
