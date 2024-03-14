#!/usr/bin/node
const list = require('./100-data').list;

let cnt = 0;
const arr = list.map((x) => x * cnt++);
console.log(list);
console.log(arr);
