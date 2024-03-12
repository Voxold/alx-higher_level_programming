#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
let num = process.argv[2] | 0;
let cnt = num;
const arr = [];
while (cnt > 0 && cnt--) {
  arr.push('X');
}
while (num > 0 && num--) {
  console.log(arr.join(''));
}
