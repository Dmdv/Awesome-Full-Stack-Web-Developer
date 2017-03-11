/**
* @Author: Anas Aboureada <AnasAboureada>
* @Date:   Tue, 7th Mar 2017, T 14:22 +01:00
* @Email:  me@anasaboureada.com
* @Project: awesome-full-stack-web-developer
* @Filename: reduced-string.js
* @Last modified by:   AnasAboureada
* @Last modified time: Sat, 11th Mar 2017, T 11:46 +01:00
* @License: MIT License
* @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
*
* @problem link: https://www.hackerrank.com/challenges/reduced-string
*/



function reduceArray(arr){
  var previousItem = arr[0];

  for (var i = 1, length = arr.length; i < length; i++){
    if(arr[i] === previousItem){
      arr.splice(i - 1, 2);
      reduceArray(arr);
    }
    previousItem   = arr[i];
  }

  return arr;
}

function processData(input) {
    var inArr      = input.split("");
    var reducedString = reduceArray(inArr).join("");
    var result     =  reducedString.length > 0 ? reducedString : 'Empty String';
    console.log(result);
    return result;
}

console.assert(processData('aaabccddd') === 'abd');
console.assert(processData('aa') === 'Empty String');
console.assert(processData('baab') === 'Empty String');
