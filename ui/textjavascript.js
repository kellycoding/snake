var urlParams = new URLSearchParams(window.location.search);
var textId = urlParams.get('id');

 var url = 'http://snake.idv2.com/snake/api/getTextById?id=' + textId;

fetch(url).then(
  function(res) { return res.json(); }
).then(function(result) {
  const title = document.querySelector('#title');
  const text = document.querySelector("#text");
  title.innerHTML = result.title;
  text.innerHTML = result.text;
});
