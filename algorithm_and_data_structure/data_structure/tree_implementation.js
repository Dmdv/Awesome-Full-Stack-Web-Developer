function Node(data){
  this.data = data;
  this.parent = null;
  this.children = [];
}

function Tree(data){
  var node = new Node(data);
  this._root = node;
}

Tree.prototype.traverseDF = function(callback){
  (function recurse(currentNode){
    console.log(currentNode)
    for (var i = 0; i < currentNode.children.length; i++){
      recurse(currentNode.children[i]);
    }
    callback(currentNode);
  })(this._root);
};

Tree.prototype.traverseBF = function(callback){
  var queue = [];

  queue.enqueue = function(value){this.push(value);}
  queue.dequeue = function(){return this.shift;}

  queue.enqueue(this._root);
  var currentTree = queue.dequeue();

  while(currentTree){
    for (var i = 0, length = currentTree.length; i < length; i++){
      queue.enqueue(currentTree.children[i]);
    }

    callback(currentTree);
    currentTree = queue.dequeue();
  }
 }

Tree.prototype.conatains = function(callback, traverse){
  return traverse.call(this, callback);
}
