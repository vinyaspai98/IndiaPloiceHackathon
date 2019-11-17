import React, { Component } from 'react';
import Button from '@material-ui/core/Button'

class Send extends Component {
  
    handleClick = () => {
    }
    render() {
    return (
      <div >
        <Button variant="contained" color="primary" onClick={handleClick}>
        Primary
      </Button>
      </div>
    )
  }
}

export default Send
