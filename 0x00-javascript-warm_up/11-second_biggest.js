#!/usr/bin/node

const numbers = process.argv.length;
const lilSmaller = process.argv.slice(2);
if (numbers < 4) {
  console.log(0);
} else {
  const CheckTest = lilSmaller.sort((a, b) => b - a);
  console.log(CheckTest[1]);
}
