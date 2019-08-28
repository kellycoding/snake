function load() {
	fetch ('http://snake.idv2.com/snake/api/getRandomPhrase?level=1')
		.then (
			function(response) {
				return response.json();
			}
		)

		.then (
			function(data) {
				var phrase = data.phrase;
				var character = document.querySelector('#character');
				character.innerHTML = phrase
				var completedPhrase = data.completedPhrase
				var phrasesleft = document.querySelector('#progress')
				phrasesleft.innerHTML = completedPhrase
			}
		)
}
load();
function submit(e) {
	const form = document.querySelector("#insert")

	var spell = form.spell.value
	const phrase = document.querySelector('#character').innerHTML

	var data = {spell, phrase}
	console.log(data)

	e.preventDefault();
	return fetch("http://snake.idv2.com/snake/api/updatePhraseTestResult",{
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
