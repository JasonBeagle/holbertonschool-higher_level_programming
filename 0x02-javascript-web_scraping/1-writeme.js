#!/usr/bin/node
const writeMe = require('fs');
writeMe.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
