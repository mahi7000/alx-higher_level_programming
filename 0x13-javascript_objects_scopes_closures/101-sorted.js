#!/usr/bin/node
const { dict } = require('./101-data.js');

const newdict = {};

for (const userId in dict) {
  const occurences = dict[userId];
  if (newdict[occurences]) {
    newdict[occurences].push(userId.toString());
  } else {
    newdict[occurences] = [userId.toString()];
  }
}

console.log(newdict);
