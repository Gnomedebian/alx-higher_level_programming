#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, 'utf8', content, (err) => {
  if (err) {
    console.error(err);
  }
});
