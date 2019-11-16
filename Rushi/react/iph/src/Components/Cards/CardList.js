/* eslint-disable no-invalid-this */
/* eslint-disable no-confusing-arrow */
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import React from 'react';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import { Typography, LinearProgress, Dialog } from '@material-ui/core';
import WarningIcon from '@material-ui/icons/Warning';
import CheckCircleIcon from '@material-ui/icons/CheckCircle';
import ExpandLessIcon from '@material-ui/icons/ExpandLess';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
// import Divider from '@material-ui/core/Divider';
// import InboxIcon from '@material-ui/icons/Inbox';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';
import AddCircleIcon from '@material-ui/icons/AddCircle';


import FullScreenDialog from './dialog'


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
        margin: 0,
        //   paddingBottom: 0,
        textAlign: 'center',
        height: 50,
        // color: theme.palette.text.secondary,
    },
    paper2: {
        // padding: 15,
        margin: 0,
        //   paddingBottom: 0,
        textAlign: 'center',

        height: 40,
        // color: theme.palette.text.secondary,
    },
    paper1: {

        //   paddingBottom: 0,
        textAlign: 'center',

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
    icon: {
        fontSize: 30,
        paddingLeft: 15,
        paddingTop: 22,
        color: '#c9c338',
    },
    icon2: {
        fontSize: 30,
        paddingLeft: 15,
        paddingTop: 22,
        color: 'green',
    },
    icon3: {
        fontSize: 25,
        // paddingLeft: 15,
        paddingTop: 6,
        // color: 'green',
    },

});

class Card extends React.Component {


    state = {
        expand: false,
        open: false,
    }

    handleExpand = () => {
        this.setState({
            expand: !this.state.expand,
            data: []
        })
    };

    handleClickOpen = () => {
        this.setState({
            open: !this.state.open
        })
    };



    handleListItemClick = (acc) => {
        console.log(acc)
        this.setState({
            open: !this.state.open
        })
    }
    getListItem() {
        const { classes, item } = this.props;
        console.log(item);

        return (
            <div>
                <Grid container spacing={3}>

                    <Grid item xs={1}>
                        <img className={classes.img} src={item.img} />
                    </Grid>
                    <Grid item xs={1}>
                        <WarningIcon className={classes.icon} />
                        {/* <CheckCircleIcon  className={classes.icon2}/> */}

                    </Grid>
                    <Grid item xs={8}>
                        <Paper className={classes.paper}>
                            <Typography>Number of results found ...</Typography>

                            {
                                !this.state.expand ?
                                    <ExpandMoreIcon className={classes.icon3} onClick={this.handleExpand} />
                                    :
                                    <ExpandLessIcon className={classes.icon3} onClick={this.handleExpand} />
                            }
                        </Paper>
                        {/* <LinearProgress /> */}
                    </Grid>



                </Grid>
                <Grid container spacing={3}>

                    <Grid item xs={5}>

                    </Grid>
                    <Grid item xs={5}>
                        <Paper>
                            <List component="nav" aria-label="main mailbox folders">
                                <ListItem
                                    button
                                    onClick={() => this.handleListItemClick('heyyy')}
                                >
                                    <ListItemIcon>
                                        <AccountCircleIcon />
                                    </ListItemIcon>
                                    <ListItemText primary="Inbox" />
                                    <ListItemIcon>
                                        <AddCircleIcon />
                                    </ListItemIcon>
                                </ListItem>
                            </List>
                            <List component="nav" aria-label="main mailbox folders">
                                <ListItem
                                    button
                                    onClick={() => this.handleListItemClick('heyyy')}
                                >
                                    <ListItemIcon>
                                        <AccountCircleIcon />
                                    </ListItemIcon>
                                    <ListItemText primary="Inbox" />
                                    <ListItemIcon>
                                        <AddCircleIcon />
                                    </ListItemIcon>
                                </ListItem>
                            </List>
                        </Paper>
                    </Grid>




                </Grid>
                <FullScreenDialog handleClickOpen={this.handleClickOpen} open={this.state.open} />

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