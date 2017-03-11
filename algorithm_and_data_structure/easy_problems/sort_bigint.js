/**
* @Author: Anas Aboureada <AnasAboureada>
* @Date:   Sat, 25th Feb 2017, T 13:49 +01:00
* @Email:  me@anasaboureada.com
* @Project: awesome-full-stack-web-developer
* @Filename: sort_bigInt.js
* @Last modified by:   AnasAboureada
* @Last modified time: Sat, 11th Mar 2017, T 12:04 +01:00
* @License: MIT License
* @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
*/



function sortTwoItems(a, b){
  if(a.length > b.length){return 1;}
  if(a.length < b.length){return -1;}

  for (var i = 0, length = a.length; i < length; i++){
    if(parseInt(a[i]) > parseInt(b[i])){return 1;}
    if(parseInt(a[i]) < parseInt(b[i])){return -1;}
  }

  return 0;
}

function bigIntSort(arr){
  var sorted = arr.sort(sortTwoItems);
  for (var i = 0, length = sorted.length; i < length; i++){
    console.log(sorted[i]);
  }
};

bigIntSort(["1", "31415926535897932384626433832795", "31415926535897932384626433832794"]);
