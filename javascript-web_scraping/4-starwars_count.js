#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    const films = JSON.parse(body).results;
    films.forEach(film => {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/18/`)) {
        count++;
      }
    });
    }
    console.log(counter);
  }
);
