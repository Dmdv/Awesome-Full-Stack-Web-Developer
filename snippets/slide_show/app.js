/**
 * @Author: Anas Aboureada <Anas>
 * @Date:   Thu, 16th Mar 2017, T 09:00 +01:00
 * @Email:  me@anasaboureada.com
 * @Last modified by:   Anas
 * @Last modified time: Mon, 20th Mar 2017, T 17:57 +01:00
 * @License: MIT License
 * @Copyright: Copyright (c) 2017 Anas Aboureada <me@anasaboureada.com>
 */



var lastSlide = 4;
var activeSlide = 0;

var slides = document.getElementsByClassName('slide');
var dots = document.getElementsByClassName('dot');

function showSlide(){
  slides[activeSlide].style.display = 'flex';
  dots[activeSlide].classList.add('active');
}

function hideSlide(){
  slides[activeSlide].style.display = 'none';
  dots[activeSlide].classList.remove('active');
}

function showNext(){
  hideSlide();
  activeSlide = (activeSlide === lastSlide) ? 0 : activeSlide + 1;
  showSlide();
}

function showPrev(){
  hideSlide();
  activeSlide = (activeSlide === 0) ? lastSlide : activeSlide - 1;
  showSlide()
}

document.querySelector('.dots ul').addEventListener('click', function(e){
  if(e.target && e.target.matches('.dot')){
    hideSlide();
    var itemId = e.target.id;
    activeSlide = parseInt(itemId.match(/\d/g)[0]);
    showSlide();
  };
});

showSlide();
document.getElementsByClassName('prev')[0].addEventListener('click', function(){showPrev();});
document.getElementsByClassName('next')[0].addEventListener('click', function(){showNext();});
setInterval(function(){showNext();}, 2000);
