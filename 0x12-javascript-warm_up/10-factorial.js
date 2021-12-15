#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
const n = parseInt(args[0]);

function factorial (n) {
  if (!n) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(n));
