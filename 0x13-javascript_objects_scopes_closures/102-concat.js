#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, data1) {
  fs.writeFile(process.argv[4], data1, 'utf8', (err) => {
    if (err) {
      console.error(error);
    }
  });
});

fs.readFile(process.argv[3], 'utf8', function (error, data1) {
  fs.appendFile(process.argv[4], data1, 'utf8', (err) => {
    if (err) {
      console.error(error);
    }
  });
});
