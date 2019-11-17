/* eslint-disable no-invalid-this */
/* eslint-disable no-confusing-arrow */
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import React from 'react';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import CardList from './CardList'




const styles = () => ({
    root: {
        width: '100%',
        height: '100%',
        minHeight: '100vh',
        backgroundColor: 'white',
        padding: 0,
    },
    paper: {
      padding: 35,
      textAlign: 'center',
      // color: theme.palette.text.secondary,
    },
    container: {
      paddingTop: 20,
      paddingLeft: 200,
      // textAlign: 'center',
      // color: theme.palette.text.secondary,
    },
    
});


class Card extends React.Component {
   
  

  handleClick = (i) => {
    
  };

  


  getListItem() {
      const { classes, data, info } = this.props;
      console.log(data);

      return(
        <div className={classes.container}>
          {
            data.map((item,index) => {
              return (<CardList item = {item} info={info}/>)
            })
          }
        </div>
      )
      
  }

  render() {
      return (
          <div>
              {this.getListItem()}
          </div>
      );
  }
}

Card.propTypes = {
    classes: PropTypes.objectOf(PropTypes.string).isRequired,
};

export default withStyles(styles)(Card);