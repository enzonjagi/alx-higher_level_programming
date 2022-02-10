const $ = window.$;
let thas = '';
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  thas = data.hello;
  $('DIV#hello').text(thas);
});
