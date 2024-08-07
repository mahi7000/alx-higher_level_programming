$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (d) {
  $('DIV#character').text(d.name);
});
