#!/usr/bin/node
const { argv } = require('node:process');

const number = parseInt(argv[2]);
if (!(isNaN(number))) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
