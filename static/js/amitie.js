$(function() {
  $("#grid_login").hide();
  $("#login-link").click(function() {
    $(this).toggleClass("open");

    if($(this).hasClass("open")) {
      $("body").css({"background-image" : "url(/images/amitie-huis-bg.jpg)"});
    }
    else {
      $("body").css({"background-image" : "url(/images/amitie-huis.jpg)"});
    }

    $("#grid_login").toggle();
  });
});