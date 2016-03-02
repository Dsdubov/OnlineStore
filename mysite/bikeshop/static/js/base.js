/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
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
    $('#list').click(function(event){event.preventDefault();$('#products .item').addClass('list-group-item');});
    $('#grid').click(function(event){event.preventDefault();$('#products .item').removeClass('list-group-item');$('#products .item').addClass('grid-group-item');});
});
/*********************
Product box
*********************/


// function goBack() {
//     window.history.back();
// }

/****************************
Static to fixed navbar
****************************/


// function FixedTopMenuOnScroll() {
//     var winHeight = $(".site-header").height();//any image,logo or header above menu
//     winHeight = winHeight - $('.navbar').height();
//     function checkMenuOnTop() {
//         if ($(window).scrollTop() > winHeight) {
//             $('.navbar').addClass("navbar-fixed-top");
//         }
//         else {
//             $('.navbar').removeClass("navbar-fixed-top");
//         }
//     }
//     checkMenuOnTop();
//     $(window).scroll(function () {
//         checkMenuOnTop();
//     });
//   }
//   FixedTopMenuOnScroll();

$(document).ready(function () {
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
     isClosed = false;

    trigger.click(function () {
      hamburger_cross();      
    });

    function hamburger_cross() {

      if (isClosed == true) {          
        overlay.hide();
        trigger.removeClass('is-open');
        trigger.addClass('is-closed');
        isClosed = false;
      } else {   
        overlay.show();
        trigger.removeClass('is-closed');
        trigger.addClass('is-open');
        isClosed = true;
      }
  }
  
  $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
  });  
});