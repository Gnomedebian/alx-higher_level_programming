#!/usr/bin/node

const SquareA = require('./5-rectangle.js');

module.exports = class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
