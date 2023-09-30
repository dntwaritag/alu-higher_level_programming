#!/usr/bin/node

function secondLargest (arr) {
  if (arr.length <= 1) {
    return 0;
  }
  arr = arr.map(Number).sort((a, b) => b - a);
  return arr[1];
}
const args = process.argv.slice(2);
console.log(secondLargest(args));
