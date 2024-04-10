#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  let count = list.length - 1;
  for (let i = 0; i < list.length; i++, count--) {
    reverse[count] = list[i];
  }
  return (reverse);
};
