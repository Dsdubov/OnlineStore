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


function goBack() {
    window.history.back();
}

/**********************
Adding to cart
**********************/
// $(document).ready(function(){
//   $( "button.btn" ).click(function(){
//     var current_button = $(this);
//     $.ajax({
//         url: "/add/",
//         type: "GET",
//         data: {"item": $(this).attr('id')},
//         success: function(data){
//           current_button.replaceWith( data );
//         }
//     });
//    });
// });