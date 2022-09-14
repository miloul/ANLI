let room=[0, ];

function AddWishlist(id) {
    if (room[id]==1)
        room[id] = 0;
    else 
        room[id]=1;
    console.log(room[id]);
}