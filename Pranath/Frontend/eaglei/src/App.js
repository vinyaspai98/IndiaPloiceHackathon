import React, { Component } from 'react';
import './App.css';
import Search from './Components/Searching/Search';
import CardList from './Components/Cards/cardList';
import Icons from './Components/Cards/mapIcon'

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
        <Search />
        
      </div>
    );
  }
}

export default App;
