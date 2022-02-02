#!/usr/bin/node
/* Get the request module */
const request = require('request');

/* Load the command line arguments (from the 2nd one) into an array */
const myargs = process.argv.slice(2);
const rurl = 'https://swapi-api.hbtn.io/api/films/' + String(myargs[0]);
/* Write the string into the file or log error to console */
request(rurl, (err, response, body) => {
  /* If there's an error log it onto the console */
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
