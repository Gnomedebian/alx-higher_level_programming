#!/usr/bin/node
const args = parseInt(process.argv[2], 10);
if (isNaN(args)) {
  console.log('Not a number');
} else if (!isNaN(args)) {
  console.log(`My number: ${args}`);
}
