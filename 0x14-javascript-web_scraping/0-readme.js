#!/usr/bin/node
/* Get the fs library for reading and writing into files */
fs = require('fs')

/* Load the command line arguments (from the 2nd one) into an array */
myargs = process.argv.slice(2)
/* Read the file and print to console */
fs.readFile(myargs[0], 'utf8', function (err,data) {
    /* If there's an error log it onto the console */
    if (err) {
      return console.log(err);
    }
    console.log(data);
  });

