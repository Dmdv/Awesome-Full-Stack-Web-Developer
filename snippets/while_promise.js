var promiseWhile = P.method(function(condition, action) {
  if (!condition()) {return;}
  return action().then(promiseWhile.bind(null, condition, action));
});
