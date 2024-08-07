$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (d) {
    $('DIV#hello').text(d.hello);
  });
});
