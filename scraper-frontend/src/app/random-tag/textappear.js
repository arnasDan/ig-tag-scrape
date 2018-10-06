var tags = [
    '#love',
    '#followback', 
    '#instagramers', 
    '#socialsteeze', 
    '#tweegram', 
    '#photooftheday', 
    '#20likes', 
    '#amazing', 
    '#smile', 
    '#follow4follow', 
    '#like4like', 
    '#look', 
    '#instalike', 
    '#igers',
    '#picoftheday', 
    '#food',
    '#instadaily', 
    '#instafollow', 
    '#followme',
    '#girl',
    '#instagood', 
    '#bestoftheday',
    '#instacool',
    '#carryme', 
    '#follow',
    '#colorful', 
    '#style',
    '#swag'
]
function randomTag(){
    var randomNumber = Math.floor(Math.random() * (tags.length));
    document.getElementById("tagtoappear").innerHTML = tags[randomNumber];
}