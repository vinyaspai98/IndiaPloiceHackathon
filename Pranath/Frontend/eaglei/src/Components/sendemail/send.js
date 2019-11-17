import React, { Component } from 'react';
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField';
import { FormControl } from '@material-ui/core';

class Send extends Component {
  
     handleClick = (e) => {
      console.log(e.target.value);
    }
    render() {
    return (
      <div >
        <FormControl>
        <TextField
          id="filled-basic"
          label="Email"
          margin="normal"
          variant="filled"
        />
        <Button variant="contained" color="primary" onClick={this.handleClick}>
        SEND
      </Button>
        </FormControl>
      </div>
    );
  }
}

export default Send;
