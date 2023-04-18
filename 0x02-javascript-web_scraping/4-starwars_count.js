#!/usr/bin/node
const request = require('request');
const characterId = '18';
let count = 0;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      if (characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
        count++;
      }
    }
    console.log(count);
  }
});
