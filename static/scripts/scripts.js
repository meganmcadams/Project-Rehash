/* Secondary to Primary Buttons */
// credit: https://www.w3schools.com/howto/howto_js_active_element.asp

// Get the container element
var btnContainer = document.getElementById("secondary-to-primary-container");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("secondary-to-primary-btn-id");

for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
      var current = document.getElementsByClassName("secondary-to-primary-btn-active");
      current[0].className = current[0].className.replace(" secondary-to-primary-btn-active", "");
      this.className += " secondary-to-primary-btn-active";
    });
  } 