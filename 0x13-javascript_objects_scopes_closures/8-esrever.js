#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  for (let i = 0; i < len / 2; i++) {
    const temp = list[i];
    list[i] = list[len - i - 1];
    list[len - i - 1] = temp;
  }
  return (list);
};
