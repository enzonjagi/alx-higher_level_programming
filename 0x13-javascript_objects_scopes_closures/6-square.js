#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
