#!/usr/bin/node
const request = require('request');
const fileUrl = process.argv[2];

request.get(fileUrl, (err, response) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
