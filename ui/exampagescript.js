fetch ('http://snake.idv2.com/snake/api/getRandomWord?level=1')
	.then (
		function(response) {
			return response.json();
		}
	)

	.then (
		function(data) {
			var word = data.word;
			var character = document.querySelector('#character');
			character.innerHTML = word
		}
	)
