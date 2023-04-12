#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.height; idx++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const Exchange = this.width;
    this.width = this.height;
    this.height = Exchange;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
