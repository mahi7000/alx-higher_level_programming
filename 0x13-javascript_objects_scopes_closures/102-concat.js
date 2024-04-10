#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');

const file1 = fs.readFileSync(argv[2], 'utf-8');
const file2 = fs.readFileSync(argv[3], 'utf-8');
const file3 = file1 + file2;

fs.writeFileSync(argv[4], file3, 'utf-8');
