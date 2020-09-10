/*!
 * Start Bootstrap - SB Admin v6.0.0 (https://startbootstrap.com/templates/sb-admin)
 * Copyright 2013-2020 Start Bootstrap
 * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-sb-admin/blob/master/LICENSE)
 */
(function ($) {
  "use strict";

  // Add active state to sidbar nav links
  var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
  $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function () {
    if (this.href === path) {
      $(this).addClass("active");
    }
  });

  // Toggle the side navigation
  $("#sidebarToggle").on("click", function (e) {
    e.preventDefault();
    $("body").toggleClass("sb-sidenav-toggled");
  });
})(jQuery);

n = new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();
if (
  document.getElementById("date") != null &&
  document.getElementById("random")
) {
  document.getElementById("date").innerHTML = m + "/" + d + "/" + y;
  document.getElementById("random").innerHTML = Date.now();
}

function showAlert() {
  alert("Account Created Successfully");
  location.replace("login.html");
}
