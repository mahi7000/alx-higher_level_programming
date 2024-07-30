#!/usr/bin/node
//computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
	  console.error(err);
  }

  const taskUser = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!taskUser[todo.userId]) {
        taskUser[todo.userId] = 1;
      } else {
	taskUser[todo.userId] += 1;
      }
    }
  });
  console.log(taskUser);
});
