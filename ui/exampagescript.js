function load() {
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
				var completedWord = data.completedWord
				var wordsleft = document.querySelector('#progress')
				wordsleft.innerHTML = completedWord
			}
		)
}
load();
function submit(e) {
	const form = document.querySelector("#insert")

	var spell = form.spell.value
	const word = document.querySelector('#character').innerHTML

	var data = {spell, word}
	console.log(data)

	e.preventDefault();
	return fetch("http://snake.idv2.com/snake/api/updateTestResult",{
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        redirect: 'follow',
        referrer: 'no-referrer',
        body: JSON.stringify(data),
    }).then (function() {
    	form.spell.value = "" 
    	load();
    })

	console.log(JSON.stringify(data))
}
const form = document.querySelector("#insert"); form.addEventListener("submit", submit);
