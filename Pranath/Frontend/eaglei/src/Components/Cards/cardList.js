import React from 'react';
import Card from './Card';

const CardList = ({ Icons }) => {

    return(
        <div>
            {
                Icons.map((user, i) =>{
                    return(
                    <Card 
                    key={i} 
                    id={Icons[i].id} 
                    name={Icons[i].name} 
                    img={Icons[i].img}
                    data={Icons[i].data}
                    />); 
                })
            }
        </div>
    );
}

export default CardList;