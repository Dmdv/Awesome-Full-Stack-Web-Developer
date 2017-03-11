/**
* @Author: Anas Aboureada <AnasAboureada>
* @Date:   Mon, 20th Feb 2017, T 18:16 +01:00
* @Email:  me@anasaboureada.com
* @Project: awesome-full-stack-web-developer
* @Filename: binary-search.js
* @Last modified by:   AnasAboureada
* @Last modified time: Sat, 11th Mar 2017, T 11:48 +01:00
* @License: MIT License
* @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
*/


/**
 * Binary Search sorted array
 * @param  {integer} input item to search floor
 * @param  {array}   data  array to search in
 * @return {boolean}       item is found or not
 */
function binarySearch(input, data) {
  if(data.length === 0){return false;}

  var left =0;
  var right = data.length - 1;
  var divider = Math.floor(data.length / 2);

  if (input === data[divider]) {
    return true;
  } else if (input > data[divider]) {
    left = divider + 1;
    return binarySearch(input, data.slice(left, right + 1));
  } else if (input < data[divider]) {
    right = divider - 1;
    return binarySearch(input, data.slice(left, right + 1));
  }
}

console.assert(binarySearch(5, [1, 2, 3, 4, 5]) === true, 'binarySearch(5)');
console.assert(binarySearch(4, [1, 2, 3, 4, 5]) === true), 'binarySearch(4)';
console.assert(binarySearch(3, [1, 2, 3, 4, 5]) === true), 'binarySearch(3)';
console.assert(binarySearch(2, [1, 2, 3, 4, 5]) === true), 'binarySearch(2)';
console.assert(binarySearch(1, [1, 2, 3, 4, 5]) === true), 'binarySearch(1)';
console.assert(binarySearch(0, [1, 2, 3, 4, 5]) === false, 'binarySearch(0)');
