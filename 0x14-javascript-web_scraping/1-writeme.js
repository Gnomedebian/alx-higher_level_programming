const fs = require('fs');
const filePath = 'process.argv[2]';
const content = 'Python is cool';

fs.writeFile(filePath, content, (err) => {
  if (err) {
    console.error(err);
  }
});
