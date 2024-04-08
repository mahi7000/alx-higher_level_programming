#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log('0');
} else {
  const args = argv.slice(2);
  const intArgs = args.sort((a, b) => a - b);
  console.log(intArgs[intArgs.length - 2]);
}
