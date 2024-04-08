#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return (a + b);
}

const result = add(parseInt(argv[2]), parseInt(argv[3]));
console.log(result);
