let room=[0, ];

function AddWishlist(id) {
    room[id] = 1;
    console.log(room[id]);
}

function DeleteWishlist(id) {
    room[id] = 0;
}