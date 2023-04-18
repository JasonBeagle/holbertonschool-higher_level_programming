#!/usr/bin/node
const getReq = require('request');
getReq.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
