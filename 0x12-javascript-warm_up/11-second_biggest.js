#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);
let largest = 0;
let secondLargest = 0;

const input = [];
if ((args[0] === undefined) || (args.length === 1)) {
  console.log(0);
} else {
  // find largest value
  for (let i = 0; i < args.length; i++) {
    input.push(parseInt(args[i]));
  }
  largest = Math.max(...input);

  // find second largest value
  for (let i = 0; i < input.length; i++) {
    if (input[i] > secondLargest && input[i] < largest) {
      secondLargest = input[i];
    }
  }
  console.log(secondLargest);
}
