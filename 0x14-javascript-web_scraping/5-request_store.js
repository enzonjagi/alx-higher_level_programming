#!/usr/bin/node
/* Get the request module */
const fs = require('fs');
const request = require('request');

/* Load the command line arguments (from the 2nd one) into an array */
const myargs = process.argv.slice(2);
/* Write the string into the file or log error to console */
request(myargs[0], (err, response, body) => {
  /* If there's an error log it onto the console */
  if (err) {
    return console.log(err);
  }
  fs.writeFile(myargs[1], response.body, (err) => {
    /* If there's an error log it onto the console */
    if (err) {
      return console.log(err);
    }
  });
});
