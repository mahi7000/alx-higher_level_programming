#!/usr/bin/node
//prints the number of movies where Wedge Antilles is present

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          count += 1;
	}
      });
    });
    console.log(count);
  }
});
