function submit() {

	const form = document.querySelector("#input_form")

	var char = form.char.value
	var level = form.level.value
	var progress = form.progress.value
	var homographs = form.homographs.value
	var homo_chars = homographs.split("")

	var data = {char, level, progress, homo_chars}

	console.log(JSON.stringify(data))

}

const submitButton = document.querySelector("#submit"); submitButton.addEventListener("click", submit);