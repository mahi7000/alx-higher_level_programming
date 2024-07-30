#!/usr/bin/node
//Reads and prints the contents of a file

const f = require('fs');
const filePath = process.argv[2];

f.readFile(filePath, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
	} else {
		console.log(data);
	}
});
