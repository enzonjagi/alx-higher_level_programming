const $ = window.$;
let thas = '';
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let i = 0; i < data.count; i++) {
    thas = data.results[i].title;
    $('UL#list_movies').append('<li>' + thas + '</li>');
  }
});
