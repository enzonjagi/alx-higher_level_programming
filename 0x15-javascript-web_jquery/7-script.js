const $ = window.$;
let thas = '';
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  thas = data.name;
  $('DIV#character').text(thas);
});
