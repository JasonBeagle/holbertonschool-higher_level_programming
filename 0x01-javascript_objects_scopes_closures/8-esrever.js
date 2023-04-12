#!/usr/bin/node

exports.esrever = function (list) {
  const switcharoo = [];
  for (let i = list.length - 1; i >= 0; i--) {
    switcharoo.push(list[i]);
  }
  return switcharoo;
};
