#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);

const size = parseInt(args[0]);
let string = '';
const x = 'X';
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      string += x;
    }
    console.log(string);
    string = '';
  }
}
