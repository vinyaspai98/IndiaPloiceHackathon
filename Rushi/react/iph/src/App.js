import React, { Component } from 'react';
import SearchAppBar from './Components/appbar';
import Card from './Components/Cards/Card';
import Icons from './Components/Cards/mapIcon';
import { height } from '@material-ui/system';
import Button from '@material-ui/core/Button';

var firebase = require('firebase');
var firebaseConfig = {
  apiKey: "AIzaSyAohuV7Slf-OS59Ufvp65nNtu0g7VjXtyg",
  authDomain: "iphack.firebaseapp.com",
  databaseURL: "https://iphack.firebaseio.com",
  projectId: "iphack",
  storageBucket: "iphack.appspot.com",
  messagingSenderId: "136761255722",
  appId: "1:136761255722:web:679031a1691cf13f24e053"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var ref = firebase.database().ref();



class App extends Component {

  constructor() {
    super()
    this.state={
        data: {
          linked_in_state: "true",
          facebook_state: "true",
          truecaller_state: "true",
          instagram_state: "true",
        },
        appOpen: false,
    }
}

componentDidMount() {
  let ref = firebase.database().ref().child("users");
  ref.on('child_changed',(snap) => {
    console.log(snap.val());
    this.setState({
      data: snap.val()
    })
  });
}


handleClick = (e) => {
  
  if(e.key === 'Enter')
  {


    var playersRef = ref.child("/");
    playersRef.update ({
      name: e.target.value,
    });
    var playersRef = ref.child("users/"+e.target.value);
    playersRef.update ({
      linked_in_state: "true",
      facebook_state: "true",
      truecaller_state: "true",
      instagram_state: "true",

    });

    this.setState({
      appOpen: true,
    })
  //   console.log(e.target.value);
  //   ref.on("value", function(data) {
  //     console.log(data.val());
   
  //  var newPlayer = data.val();
  //  console.log("name : " + newPlayer.age);
   
   
  //  }, function (error) {
  //     console.log("Error: " + error.code);
  //  });
  }
}

  render(){
    return (
      <div >
        <SearchAppBar  handleClick={this.handleClick}/>
        {
          this.state.appOpen?
          <Card data={Icons} info={this.state.data}/>
          :null
        }
      <input
      accept="image/*"
      style={{ display: 'none' }}
      id="raised-button-file"
      multiple
      type="file"
    />
   
    <label htmlFor="raised-button-file">
      <Button variant="raised" component="span" >
        Upload
      </Button>
    </label>
    </div>
    );
  }
}

export default App;
