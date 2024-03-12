#!/usr/bin/node
let len = process.argv.length; const arr = [];
if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  len = arr.length;
  arr.sort((a, b) => a - b);
  console.log(arr[len - 2]);
}
