#!/usr/bin/node
const readME = require('fs');
readME.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
