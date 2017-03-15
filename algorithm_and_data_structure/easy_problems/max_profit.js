/**
* @Author: Anas Aboureada <anas>
* @Date:   Tue, 14th Mar 2017, T 13:41 +01:00
* @Email:  me@anasaboureada.com
* @Project: awesome-full-stack-web-developer
* @Filename: max_profit.js
* @Last modified by:   anas
* @Last modified time: Tue, 14th Mar 2017, T 15:04 +01:00
* @License: MIT License
* @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
*
* @Problem_url: https://www.interviewcake.com/question/python/stock-price
*/



function getMaxProfitNaive(stockPricesArr){
  var currentBuyIndex = 0;
  var maxProfit = -100000000;

  for (var i = 1, length = stockPricesArr.length; i < length; i++){

    for (var j = i; j < length; j++){
      var currentProfit = stockPricesArr[j] - stockPricesArr[currentBuyIndex];
      if(currentProfit > maxProfit){
        maxProfit = currentProfit;
      }
      currentBuyIndex = i;
    }
  }
  return maxProfit;
}


function getMaxProfitDevide(stockPricesArr){
  var stockPricesArrLength = stockPricesArr.length;

  if(stockPricesArrLength <= 1){return 0;}

  var right = stockPricesArr.slice(0, stockPricesArrLength / 2);
  var left = stockPricesArr.slice(stockPricesArrLength / 2, stockPricesArrLength);

  var maxLeft = getMaxProfitDevide(left);
  var maxRight = getMaxProfitDevide(right);


  var crossProfit = Math.max.apply(null, left) - Math.min.apply(null, right);

  return Math.max(crossProfit, maxRight, maxLeft)
}

function getMaxProfitDynamic(stockPricesArr){

  var cheapest = stockPricesArr[0];
  var profit = -1000000;

  for (var i = 1, length = stockPricesArr.length; i < length; i++){
      if(stockPricesArr[i] < cheapest){cheapest = stockPricesArr[i]}
      profit = Math.max(profit, stockPricesArr[i] - cheapest);
  }
  return profit;
}

var stockPricesYesterday = [10, 7, 5, 8, 11, 9];
console.assert(getMaxProfitNaive(stockPricesYesterday) === 6);
console.assert(getMaxProfitDevide(stockPricesYesterday) === 6);
console.assert(getMaxProfitDynamic(stockPricesYesterday) === 6);
