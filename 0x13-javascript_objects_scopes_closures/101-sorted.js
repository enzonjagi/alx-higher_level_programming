#!/usr/bin/node
const dict = require('./101-data').dict;
const createdDict = {};
for (const key in dict) {
  if (createdDict[dict[key]]) {
    createdDict[dict[key]].push(key);
  } else {
    createdDict[dict[key]] = [key];
  }
}
console.log(createdDict);
