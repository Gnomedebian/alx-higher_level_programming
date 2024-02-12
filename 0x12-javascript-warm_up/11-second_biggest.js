#!/usr/bin/node
function nextBiggest (myArr) {
  let maxNum = 0;
  let result = 0;
  for (const value of myArr) {
    const n = Number(value);

    if (n > maxNum) {
      [result, maxNum] = [maxNum, n];
    } else if (n < maxNum && n > result) {
      result = n;
    }
  }

  return result;
}

console.log(nextBiggest(process.argv));
