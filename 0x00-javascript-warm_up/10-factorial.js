#!/usr/bin/node

const isFact = process.argv[2];

function factorial (isFact) {
  if (isNaN(isFact) || isFact <= 1) {
    return 1;
  } else {
    return isFact * factorial(isFact - 1);
  }
}
console.log(factorial(isFact));
