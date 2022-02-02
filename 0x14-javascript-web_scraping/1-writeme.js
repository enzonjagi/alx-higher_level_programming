#!/usr/bin/node
/* Get the fs library for reading and writing into files */
const fs = require('fs');

/* Load the command line arguments (from the 2nd one) into an array */
const myargs = process.argv.slice(2);
/* Write the string into the file or log error to console */
fs.writeFile(myargs[0], myargs[1], (err) => {
  /* If there's an error log it onto the console */
  if (err) {
    return console.log(err);
  }
});
