/**
* @Author: Anas Aboureada <anas>
* @Date:   Tue, 14th Mar 2017, T 13:59 +01:00
* @Email:  me@anasaboureada.com
* @Project: awesome-full-stack-web-developer
* @Filename: staircase.js
* @Last modified by:   anas
* @Last modified time: Tue, 14th Mar 2017, T 14:05 +01:00
* @License: MIT License
* @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
* @Problem_url: https://www.hackerrank.com/challenges/staircase
*/



function printStairCase(n){

  for(var i = 1; i <= n; i++){
    var stairStep = "";
    for(var j = 1; j <= n - i; j++){
      stairStep += " ";
    }

    for(var k = 1; k <= i; k++){
      stairStep += "#";
    }
    console.log(stairStep);
  }
}

printStairCase(10);
