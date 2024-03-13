#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (const item of list) {
    if (item === searchElement) { cnt++; }
  }
  return (cnt);
};
