#!/usr/bin/node
const { list } = require('./100-data.js');

const mapped = list.map((num, index) => num * index);

console.log(list);
console.log(mapped);
