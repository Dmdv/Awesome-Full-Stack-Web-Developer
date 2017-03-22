<!--
@Author: Anas Aboureada <anas>
@Date:   Mon, 20th Mar 2017, T 13:46 +01:00
@Email:  me@anasaboureada.com
@Filename: nodejs_questions.md
@Last modified by:   anas
@Last modified time: Mon, 20th Mar 2017, T 18:26 +01:00
@License: MIT License
@Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
-->

# Node.js Questions and answers

### Q: Consider the following JavaScript code:

```javascript
console.log("first");
setTimeout(function() {
    console.log("second");
}, 0);
console.log("third");
```

The output will be:

    first
    third
    second

Assuming that this is the desired behavior, and that we are using Node.js version 0.10 or higher, how else might we write this code?

#### Answer:

Node.js version 0.10 introduced `setImmediate`, which is equivalent to `setTimeout(fn, 0)`, but with some slight advantages.

`setTimeout(fn, delay)` calls the given callback fn after the given delay has ellapsed (in milliseconds). However, the callback is not executed immediately at this time, but added to the function queue so that it is executed as soon as possible, after all the currently executing and currently queued event handlers have completed. Setting the delay to 0 adds the callback to the queue immediately so that it is executed as soon as all currently-queued functions are finished.

`setImmediate(fn)` achieves the same effect, except that it doesn’t use the queue of functions. Instead, it checks the queue of I/O event handlers. If all I/O events in the current snapshot are processed, it executes the callback. It queues them immediately after the last I/O handler somewhat like process.nextTick. This is faster than `setTimeout(fn, 0)`.

So, the above code can be written in Node as:

```javaScript
console.log("first");
setImmediate(function(){
    console.log("second");
});
console.log("third");
```

* * *

### Q: What is the preferred method of resolving unhandled exceptions in Node.js?

#### Answer:

Unhandled exceptions in Node.js can be caught at the Process level by attaching a handler for uncaughtException event.

```javaScript
process.on('uncaughtException', function(err) {
  console.log('Caught exception: ' + err);
});
```

However, uncaughtException is a very crude mechanism for exception handling and may be removed from Node.js in the future. An exception that has bubbled all the way up to the Process level means that your application, and Node.js may be in an undefined state, and the only sensible approach would be to restart everything.

The preferred way is to add another layer between your application and the Node.js process which is called the domain.

Domains provide a way to handle multiple different I/O operations as a single group. So, by having your application, or part of it, running in a separate domain, you can safely handle exceptions at the domain level, before they reach the Process level.
