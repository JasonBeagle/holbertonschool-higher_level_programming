#!/usr/bin/node

const oneArg = process.argv;

if (!oneArg[2]) {
  console.log('No argument');
} else {
  console.log(oneArg[2]);
}
