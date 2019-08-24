function submit() {

	const form = document.querySelector("#input_form")

	var char = form.char.value
	var spell = form.spell.value
	var level = form.level.value
	var progress = form.progress.value
	var homographs = form.homographs.value
	var homo_chars = homographs.split("")

	var data = {char, spell, level, progress, homo_chars}

	 return fetch("http://snake.idv2.com/snake/api/createWord",{
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        redirect: 'follow',
        referrer: 'no-referrer',
        body: JSON.stringify(data),
    }).then (
    	loadwords
    )

	console.log(JSON.stringify(data))

}

function loadwords() {
	fetch ('http://snake.idv2.com/snake/api/getWordFullList')
	.then (
		function(response) {
			return response.json();
		}
	).then(function(result) {
		var tbody = document.querySelector("#tbody");

		var child = tbody.lastElementChild;  
        while (child) { 
        	tbody.removeChild(child); 
        	child = tbody.lastElementChild; 
		}

		for (var i = 0; i < result.words.length; i++) {
			var word = result.words[i];

			var tr = document.createElement('tr');

			var td1 = document.createElement('td');
			var td2 = document.createElement('td');
			var td3 = document.createElement('td');
			var td4 = document.createElement('td');
			var td5 = document.createElement('td');

			td1.innerHTML = word.name;
			td2.innerHTML = word.level.name;
			td3.innerHTML = word.proficiency.count;
			td4.innerHTML = word.homographs.map(h => h.name);
			td5.innerHTML = word.spell;

			tr.appendChild(td1);
			tr.appendChild(td2);
			tr.appendChild(td3);
			tr.appendChild(td4);
			tr.appendChild(td5);

			tbody.appendChild(tr);
		}
	})
}

loadwords();
const submitButton = document.querySelector("#submit"); submitButton.addEventListener("click", submit);