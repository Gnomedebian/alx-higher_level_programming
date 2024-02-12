#!/usr/bin/node
function fact (i) {
  return i === 0 || isNaN(i) ? 1 : i * fact(i - 1);
}

console.log(fact(Number(process.argv[2])));
