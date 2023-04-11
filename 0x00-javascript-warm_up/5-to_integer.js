#!/usr/bin/node

const numCheck = parseInt(process.argv[2]);
if (isNaN(numCheck)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + numCheck);
}
