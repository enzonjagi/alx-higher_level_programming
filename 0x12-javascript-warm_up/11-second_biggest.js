#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);
let largest = 0;
let secondLargest = 0;

if ((args[0] === undefined) || (args.length === 1)) {
  console.log(0);
} else {
  // find largest value
  for (let i = 0; i < args.length; i++) {
    if (args[i] > largest) {
      largest = args[i];
    }
  }
  // find second largest value
  for (let i = 0; i < args.length; i++) {
    if (args[i] > secondLargest && args[i] < largest) {
      secondLargest = args[i];
    }
  }
  console.log(secondLargest);
}
