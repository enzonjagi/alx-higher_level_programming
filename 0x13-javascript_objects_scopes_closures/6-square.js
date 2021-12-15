#!/usr/bin/node
const ogsquare = require('./5-square');

class Square extends ogsquare {
  charPrint (c) {
    let input = c;
    if (!c) {
      input = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(input.repeat(this.width));
    }
  }
}

module.exports = Square;
