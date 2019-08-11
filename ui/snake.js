const cvs = document.getElementById("snake");
const ctx = cvs.getContext("2d");
const startGameButton = document.querySelector("#start_game"); startGameButton.addEventListener("click", start_game);
const title = document.querySelector("#title")
const gameover = document.querySelector("#gameover")

var homographs = {}
var key = ""
var value = ""

fetch ('http://snake.idv2.com/snake/api/getRandomSentence')
	.then (
		function(response) {
			return response.json();
		}
	)

	.then (
		function(data) {
			var sentence = data.sentence;
			homographs = data.homographs;

			var title = document.querySelector('#hint');
			title.innerHTML = sentence;
			console.log(homographs)

			var keys = Object.keys(homographs);
			key = keys[Math.floor(Math.random()*keys.length)];
			value = homographs[key]

		}
	)

//start game
function start_game(){
	title.style.display = 'none'
	//create the unit

	const box = 32;

	//load images

	const ground = new Image();
	ground.src = "img/ground.png";

	const foodImage = new Image();
	foodImage.src = "img/food.png";

	const heartImage = new Image();
	heartImage.src = "img/heart.png";

	const bombImage = new Image();
	bombImage.src = "img/bomb.png";

	// load audio files
	const dead = new Audio();

	dead.src = "audio/dead.mp3"

	const explosion = new Audio();

	explosion.src = "audio/explbomb.wav"

	const eat = new Audio();

	eat.src = "audio/eat.wav"
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

	//create the bombs

	let bomb = {
		x : Math.floor(Math.random()*17+1) * box,
		y : Math.floor(Math.random()*15+3) * box
	}

	//create the score var

	let score = 0;

	//create the lives var

	let lives = 3;

	//control the snake

	let d;

	document.addEventListener("keydown",direction)

	function direction(event){
		let key = event.keyCode
		if(key == 37 && d != "RIGHT"){
			d = "LEFT";
		}else if(key == 38 && d != "DOWN"){
			d = "UP";
		}else if(key == 39 && d != "LEFT"){
			d = "RIGHT";
		}else if(key == 40 && d != "UP"){
			d = "DOWN";
		}
	}

	// check collision function
	function collision(head,array){
		for(let i = 0; i < array.length; i++){
			if(head.x == array[i].x && head.y == array[i].y){
				return true;
			}
		}
		return false;
	}

	//draw everything to the canvas

	function draw(){

		ctx.drawImage(ground,0,0);

		for( let i = 0; i < snake.length ; i++){
			ctx.fillStyle = ( i == 0 )? "green" : "white";
			ctx.fillRect(snake[i].x,snake[i].y,box,box);

			ctx.strokeStyle = "red";
			ctx.strokeRect(snake[i].x,snake[i].y,box,box);
		}

		ctx.font = '28px Microsoft Yahei';
		ctx.textBaseline = "top";
		ctx.fillStyle = "white";
		ctx.fillText(key, food.x, food.y);
		ctx.fillText(value, bomb.x, bomb.y);
		ctx.drawImage(heartImage,570,20)

		// old head position
		let snakeX =snake[0].x;
		let snakeY =snake[0].y;

		//which direction
		if(d == "LEFT") snakeX -= box;
		if(d == "UP") snakeY -= box;
		if(d == "RIGHT") snakeX += box;
		if(d == "DOWN") snakeY += box;

		//if the snake eats the food
		if(snakeX == food.x && snakeY == food.y){
			score++;

			var keys = Object.keys(homographs);
			key = keys[Math.floor(Math.random()*keys.length)];
			value = homographs[key]

			eat.play();
			bomb = {

				x : Math.floor(Math.random()*17+1) * box,
				y : Math.floor(Math.random()*15+3) * box
			}
			food = {
				x : Math.floor(Math.random()*17+1) * box,
				y : Math.floor(Math.random()*15+3) * box
			}
			//we don't remove its tail
		}else{
			//remove the tail
			snake.pop();
		}

		//add new head

		let newHead = {
			x : snakeX,
			y: snakeY
		}

		//if the snake touches the bomb
		if(snakeX == bomb.x && snakeY == bomb.y){
			lives--;

			var keys = Object.keys(homographs);
			key = keys[Math.floor(Math.random()*keys.length)];
			value = homographs[key]

			explosion.play();
			food = {
				x : Math.floor(Math.random()*17+1) * box,
				y : Math.floor(Math.random()*15+3) * box
			}
			bomb = {
				x : Math.floor(Math.random()*17+1) * box,
				y : Math.floor(Math.random()*15+3) * box
			}
		}else{
		}

		//if lives run out
		if(lives == 0){
			clearInterval(game);
			dead.play();
			game_over();

		}else{
		}


		//game over

		if(snakeX < box || snakeX > 17 * box || snakeY < 3*box || snakeY > 17*box || collision(newHead,snake)){
			clearInterval(game);
			dead.play();
			game_over();
		}

		snake.unshift(newHead);

		ctx.fillStyle = "white";
		ctx.font = "45px Changa One";
		ctx.fillText(score,2*box,0.6*box);
		ctx.fillText(lives,17*box,0.6*box);
	}

	//call draw function every 100 ms

	let game = setInterval(draw,100);

	//game over
	function game_over(){
		gameover.style.display = 'block'
		ctx.clearRect(0, 0, 608, 608)
		document.removeEventListener("keydown",direction)

	}

}