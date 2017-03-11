/**
* @Author: Anas Aboureada <AnasAboureada>
* @Date:   Sat, 11th Mar 2017, T 12:35 +01:00
* @Email:  me@anasaboureada.com
* @Project: awesome-full-stack-web-developer
* @Filename: 2d-array.js
* @Last modified by:   AnasAboureada
* @Last modified time: Sat, 11th Mar 2017, T 12:36 +01:00
* @License: MIT License
* @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
*
* @problem link: https://www.hackerrank.com/challenges/2d-array
*/



function sumHourGlass(i, j, arr){
    var hourGlassSum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] +
        arr[i + 2][j] +
        arr[i + 2][j + 1] + arr[i + 2][j + 2];
    return hourGlassSum;
}

function main() {
    var arr = [];
    for(arr_i = 0; arr_i < 6; arr_i++){
       arr[arr_i] = readLine().split(' ');
       arr[arr_i] = arr[arr_i].map(Number);
    }
    var maxSum = -1000000;

    for (var i = 0; i < 4; i++){
        for(var j = 0; j < 4; j++){
            var hourGlassSum =  sumHourGlass(i, j, arr);
            if (hourGlassSum > maxSum){maxSum = hourGlassSum;}
        }
    }

    console.log(maxSum);
}
