#!/usr/bin/node
const request = require('request');
const fileUrl = process.argv[2];

request.get(fileUrl, (error, response) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code: ' + response.statusCode);
});
