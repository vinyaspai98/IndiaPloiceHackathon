import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import ListItemText from '@material-ui/core/ListItemText';
import ListItem from '@material-ui/core/ListItem';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import CloseIcon from '@material-ui/icons/Close';
import Slide from '@material-ui/core/Slide';
import Grid from '@material-ui/core/Grid';

const useStyles = makeStyles(theme => ({
    appBar: {
        position: 'relative',
    },
    img: {
        paddingTop: 25,
        width: 150,
        height: 150,
    },
    title: {
        marginLeft: theme.spacing(2),
        flex: 1,
    },
}));

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
});

export default function FullScreenDialog({ handleClickOpen, open }) {
    const classes = useStyles();




    return (
        <div>

            <Dialog fullScreen open={open} onClose={handleClickOpen} TransitionComponent={Transition}>
                <AppBar className={classes.appBar}>
                    <Toolbar>
                        <IconButton edge="start" color="inherit" onClick={handleClickOpen} aria-label="close">
                            <CloseIcon />
                        </IconButton>
                        <Typography variant="h6" className={classes.title}>
                            Profile-Data
                        </Typography>
                        <Button autoFocus color="inherit" onClick={handleClickOpen}>
                            save
                        </Button>
                    </Toolbar>
                </AppBar>

                <Grid container spacing={3}>

                    <Grid item xs={5}>
                    </Grid>
                    <Grid item xs={1}>
                        <img className={classes.img} src='/images/search.svg' />
                    </Grid>
                    



                </Grid>

                <List>
                    <ListItem button>
                        <ListItemText primary="Phone ringtone" secondary="Titania" />
                    </ListItem>
                    <Divider />
                    <ListItem button>
                        <ListItemText primary="Default notification ringtone" secondary="Tethys" />
                    </ListItem>
                </List>
            </Dialog>
        </div>
    );
}
