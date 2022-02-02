#!/usr/bin/node
/* Get the request module */
const request = require('request');
const fs = require('fs');

/* Load the command line arguments (from the 2nd one) into an array */
const myargs = process.argv.slice(2);
const count = 0;
/* Write the string into the file or log error to console */
request(myargs[0], (err, response, body) => {
  /* If there's an error log it onto the console */
  if (err) {
    return console.log(err);
  }
  const obj = JSON.parse(body);

  const dict = {};
  let count;
  for (let x = 1; x <= 10; x++) {
    dict.key = x;
    count = 0;
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].userId === x && obj[i].completed === true) {
        count += 1;
      }
    }
    dict[x] = count;
  }
  delete dict.key;
  console.log(dict);
});
