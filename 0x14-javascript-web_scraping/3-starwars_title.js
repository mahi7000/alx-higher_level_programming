#!/usr/bin/node
// print the title of Star Wars movie

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const title = JSON.parse(body);
    console.log(`${title.title}`);
  }
});
