function loadtexts() {
	fetch ('http://snake.idv2.com/snake/api/getTextList')
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

		for (var i = 0; i < result.texts.length; i++) {
			var text = result.texts[i];

			var tr = document.createElement('tr');

			var td = document.createElement('td');

			td.innerHTML = text.title;

			tr.appendChild(td);

			tbody.appendChild(tr);
		}
	})
}
loadtexts();