import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

const Card = ({ name, img, id, data}) => {
  const classes = useStyles();

  return (
    <div className="ma2">
        <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={3}>
          <Paper className={classes.paper}>{ img }</Paper>
        </Grid>
        <Grid item xs={9}>
          <Paper className={classes.paper}>data from firebase</Paper>
        </Grid>
      </Grid>
    </div>
    </div>
  );
}

export default Card;
