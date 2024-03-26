#!/usr/bin/node
const fs = require('fs');

const filePath = 'cisfun';

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
