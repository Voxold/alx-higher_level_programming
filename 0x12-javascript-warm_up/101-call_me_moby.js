#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  while (x && x > 0) {
    func();
    x--;
  }
};
