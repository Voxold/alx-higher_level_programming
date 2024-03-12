#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
let num = process.argv[2] | 0;
while (num > 0 && num--) {
  console.log('C is fun');
}
