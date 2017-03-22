// Promise while that return promise 

var P = require('bluebird');

var promiseWhile = P.method(function(condition, action) {
  if (!condition()) {return;}
  return action().then(promiseWhile.bind(null, condition, action));
});

/*
  Usage:
 */

var condition = true;
promiseWhile(function() { return condition; }, function() {
// some promise logic that will set condition to false at some point;
});
