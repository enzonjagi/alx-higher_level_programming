#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);

const intValue = parseInt(args[0]);

if (isNaN(intValue)) {
  console.log('Not a number');
} else {
  console.log('My number:', intValue);
}
