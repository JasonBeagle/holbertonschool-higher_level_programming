#!/usr/bin/node

const howMany = process.argv[2];
if (isNaN(howMany)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < howMany; i++) { console.log('C is fun'); }
}
