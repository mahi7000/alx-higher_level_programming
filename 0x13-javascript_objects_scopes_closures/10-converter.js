#!/usr/bin/node

exports.converter = function (base) {
  function myConvert (item) {
    return (item.toString(base));
  }
  return (myConvert);
};
