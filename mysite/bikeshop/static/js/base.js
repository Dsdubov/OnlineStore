function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}


/*********************
Product box
*********************/
$(document).ready(function() {
    $('#list').click(function(event){
      event.preventDefault();
      $('#products .item').addClass('list-group-item');
       document.getElementById('description').style.display='block';
    });
    $('#grid').click(function(event){
      event.preventDefault();
      $('#products .item').removeClass('list-group-item');$
      ('#products .item').addClass('grid-group-item');
       document.getElementById('description').style.display='none';
    });
});
/*********************
Product box
*********************/

$(document).ready(function () {
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
      leftBlock = $('.left-block'),
     isClosed = true;
     if (document.documentElement.clientWidth < 768) {
      trigger.show();
      $('#wrapper').removeClass('toggled');
      $('#header').css({'marginLeft' : 0});
    }
    trigger.click(function () {
      hamburger_cross();      
    });
    function hamburger_cross() {

      if (isClosed == true) {          
        overlay.hide();
        leftBlock.show();
        trigger.removeClass('is-open');
        trigger.addClass('is-closed');
        $('#header').animate({'marginLeft' : 220}, {'duration' : 500});
        // $('#wrap').animate({'marginLeft' : 0}, {'duration' : 100});
        isClosed = false;
      } else {   
        overlay.show();
        leftBlock.hide();
        $('#header').animate({'marginLeft' : 0}, {'duration' : 500});
        // $('#wrap').animate({'marginLeft' : 220}, {'duration' : 100});
        trigger.removeClass('is-closed');
        trigger.addClass('is-open');
        isClosed = true;
      }
  }
  
  $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
  });  
});
