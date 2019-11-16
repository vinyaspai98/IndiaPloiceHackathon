/* eslint-disable no-invalid-this */
/* eslint-disable no-confusing-arrow */
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import React from 'react';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import { Typography } from '@material-ui/core';


const styles = () => ({
    root: {
        width: '100%',
        height: '100%',
        minHeight: '100vh',
        backgroundColor: 'white',
        padding: 0,
    },
    paper: {
      padding: 15,
      textAlign: 'center',
      height: 50,
      // color: theme.palette.text.secondary,
    },
    container: {
      paddingTop: 20,
      // textAlign: 'center',
      // color: theme.palette.text.secondary,
    },
    img: {
      width: 80,
      height: 80,
      borderRadius: 20,
      // textAlign: 'center',
      // color: theme.palette.text.secondary,
    },
    
});

class Card extends React.Component {



  getListItem() {
      const { classes, item } = this.props;
      console.log(item);

      return(
        <div>
    <Grid container spacing={3}>
       
        <Grid item xs={1}>
          <img className={classes.img} src={item.img}/>
        </Grid>
        <Grid item xs={8}>
          <Paper className={classes.paper}>
              <Typography>Number of results found ...</Typography>
          </Paper>
        </Grid>
       
      </Grid>
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