#!/usr/bin/node

const xSquare = process.argv[2];
if (isNaN(xSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < xSquare; i++) {
    console.log('X'.repeat(xSquare));
  }
}
