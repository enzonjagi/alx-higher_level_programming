#!/usr/bin/node
const array = require('./100-data');
const createdArray = array.list.map((elem, idx) => elem * idx);
console.log(array.list);
console.log(createdArray);
