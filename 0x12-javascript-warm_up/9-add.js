#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);

const first = parseInt(args[0]);
const second = parseInt(args[1]);
if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  const add = first + second;
  console.log(add);
}
