#!/usr/bin/node
const dic = require('./101-data').dict;
const newDic = {};
for (const key in dic) {
  if (newDic[dic[key]] === undefined) { newDic[dic[key]] = [key]; } else { newDic[dic[key]].push(key); }
}
console.log(newDic);
