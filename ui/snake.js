const cvs = document.getElementById("snake");
const ctx = cvs.getContext("2d");

//create the unit

const box = 32;

//load images

const ground = new Image();
ground.src = "img/ground.png";

const foodImage = new Image();
foodImage.src = "img/food.png";

//create the snake

let snake = [];
snake[0] = {
	x : 9 * box,
	y : 10 * box
}

//create the food

let food = {
	x : Math.floor(Math.random()*17+1) * box,
	y : Math.floor(Math.random()*15+3) * box
}

//create the score var

let score = 0;

//draw everything to the canvas

function draw(){

	ctx.drawImage(ground,0,0);

	for( let i = 0; i < snake.length ; i++){
		ctx.fillStyle = ( i == 0 )? "green" : "white";
		ctx.fillRect(snake[i].x,snake[i].y,box,box);

		ctx.strokeStyle = "red";
		ctx.strokeRect(snake[i].x,snake[i].y,box,box);
	}

	ctx.drawImage(foodImg, food.x, food.y)
}

//call draw function every 100 ms

let game = setInterval(draw,100);