import React, { Component } from 'react';
import SearchAppBar from './Components/appbar';
import CardList from './Components/Cards/cardList';
import Icons from './Components/Cards/mapIcon';

class App extends Component {

  constructor() {
    super()
    this.state={
        Icons: Icons,
    }
}

  render(){
    return (
      <div >
        <SearchAppBar />
        {/* <CardList Icons={this.state.Icons} /> */}
      </div>
    );
  }
}

export default App;
