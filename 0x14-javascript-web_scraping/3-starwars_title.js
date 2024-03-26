#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = ('https://swapi-api.alx-tools.com/api/films/' + movieId);

request.get(apiUrl, (error, _, response) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(response);
    console.log(content.title);
  }
});
