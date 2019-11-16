import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    paddingLeft: 220,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
  paper1: {
    padding: theme.spacing(2),
    width: 200,
    height: 200,
    textAlign: 'center',
    color: theme.palette.text.secondary,
    borderRadius: 20,
  },
  paper2: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    height: 70,
  },
}));

const Card = ({ name, img, id, data}) => {
  const classes = useStyles();

  return (
        <div className="ma3">
        <div className={classes.root}>
        <Grid container spacing={3}>
          <Grid item xs={1} >
            <Paper className={classes.paper1}><img src={`${img}`} /></Paper>
          </Grid>
          {/* <Grid item xs={1} >
            hey
          </Grid> */}
          <Grid item xs={7}>
            <Paper className={`sizing ${classes.paper2}`}>data from firebase</Paper>
          </Grid>
        </Grid>
    </div>
    </div>
  );
}

export default Card;
