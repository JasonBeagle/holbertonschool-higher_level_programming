#!/usr/bin/node

const argCnt = process.argv.length;

if (argCnt === 2) {
  console.log('No argument');
} else if (argCnt === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
