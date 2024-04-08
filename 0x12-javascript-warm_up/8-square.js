#!/usr/bin/node
const { argv } = require('node:process');

const x = parseInt(argv[2]);
let square = '';
if (isNaN(x)) {
  console.log('Missing size');
} else if (x > 0) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    if (i !== x - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
