/**
* @Author: Anas Aboureada <AnasAboureada>
* @Date:   Wed, 9th Nov 2016, T 11:44 +01:00
* @Email:  me@anasaboureada.com
* @Project: awesome-full-stack-web-developer
* @Filename: sort_json.js
* @Last modified by:   AnasAboureada
* @Last modified time: Sat, 11th Mar 2017, T 14:10 +01:00
* @License: MIT License
* @Copyright: Copyright (c) 2017 Anas Aboureada <anasaboureada.com>
*/



var sampleOcr = require('./ocr-playhead-edited.json');
var _         = require('lodash');

/**
 * Sorting input array of json objects 
 * @type {Number}
 */
(function sortJson(ocrJson) {
  var currentY    = 0;
  var currentRow  = 0;
  var currentPage = 0;
  var currentItem = 0;
  var namedRow    = 1;

  var initialSorted = _.sortBy(ocrJson, ['page', 'y', 'x']);
  var newOcr        = _.map(initialSorted, function(item) {

    if (item.page > currentPage) {
      currentPage += 1;
      currentY = 0;
    }

    if (Math.abs(item.y - currentY) > 0.05) {
      currentRow += 1;
    }

    item.system = currentRow;
    currentY = item.y;

    return item;
  });

  var sortedOcr = _.sortBy(newOcr, ['page', 'system', 'x']);
  var namedOcr  = _.map(sortedOcr, function(ocrItem) {

    if (ocrItem.system === namedRow) {
      currentItem += 1;
    } else {
      namedRow    = ocrItem.system;
      currentItem = 1;
    }

    ocrItem.name = namedRow + '.' + currentItem;
    return ocrItem;
  });

  console.log(JSON.stringify(namedOcr));
  return namedOcr;

}(sampleOcr.playback_positions));
