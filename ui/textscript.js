function submit(e) {
	const form = document.querySelector("#form")

	var passage = form.passage.value
	var title = form.title.value

	var data = {text: passage, title: title}
	console.log(data)

	e.preventDefault();
	return fetch("http://snake.idv2.com/snake/api/createText",{
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
        },
        redirect: 'follow',
        referrer: 'no-referrer',
        body: JSON.stringify(data),
    }).then (function() {
    	form.passage.value = "" 
    })

	console.log(JSON.stringify(data))
}
const form = document.querySelector("#form"); form.addEventListener("submit", submit);