#!/usr/bin/node

const process = require('process');

const args = process.argv;

if (args.length < 3) {
  console.log('No Argument');
} else {
  console.log('Argument Found');
}
