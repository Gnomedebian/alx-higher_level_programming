#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const endPoint = {};
    for (const x of data) {
      if (x.endPoint === true) {
        if (x.userId in endPoint) {
          endPoint[x.userId]++;
        } else {
          endPoint[x.userId] = 1;
        }
      }
    }
    console.log(endPoint);
  }
});
