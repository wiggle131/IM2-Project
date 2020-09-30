var childdiv;
$(document).on("click", ".getStatus", function () {
  var str = $("#status").val();

  var html = "";

  if (str.length === 7) {
    html =
      '<div class="form-row mt-6 spouse"><div class="col-12 col-sm-6"><input class=" form-control"type="text" placeholder="Spouse Name" name="spousename"/> </div> <div class="col-12 col-sm-6 mt-4 mt-sm-0"> <input class="form-control" type="text" placeholder="Spouse Occupation" name="spouseoccupation" /> </div> </div>';

    $(".personal").prepend(html);
  } else if (str.length == 6) {
    childdiv = $(".child");
    $(".child").remove();
    $(".mothername").addClass("col-sm-6");
    $(".fathername").addClass("col-sm-6");
  }
});

$("#prev").click(function () {
  if (!$(".personal").hasClass("child")) {
    $(".personal-1").prepend(childdiv);
  }
  $(".spouse").remove();
  $(".mothername").removeClass("col-sm-6");
  $(".fathername").removeClass("col-sm-6");
});

$(document).ready(function () {
  $("#elem").hide();
  $("#junior").hide();
  $("#senior").hide();
  $("#college").hide();
  $("#post").hide();
  $("#training-0").hide();
});

$("#eduTab").click(function () {
  if ($("#elemSchool").val().length > 0) {
    $("#elem").toggle();
    $("#addElem").prop("value", "Remove");
  }
  if ($("#juniorSchool").val().length > 0) {
    $("#junior").toggle();
    $("#addJunior").prop("value", "Remove");
  }
  if ($("#seniorSchool").val().length > 0) {
    $("#senior").toggle();
    $("#addSenior").prop("value", "Remove");
  }
  if ($("#collegeSchool").val().length > 0) {
    $("#college").toggle();
    $("#addCollege").prop("value", "Remove");
  }
  if ($("#postSchool").val().length > 0) {
    $("#post").toggle();
    $("#addPost").prop("value", "Remove");
  }
});

$("#eduNext").click(function () {
  if ($("#elemSchool").val().length > 0) {
    $("#elem").toggle();
    $("#addElem").prop("value", "Remove");
  }
  if ($("#juniorSchool").val().length > 0) {
    $("#junior").toggle();
    $("#addJunior").prop("value", "Remove");
  }
  if ($("#seniorSchool").val().length > 0) {
    $("#senior").toggle();
    $("#addSenior").prop("value", "Remove");
  }
  if ($("#collegeSchool").val().length > 0) {
    $("#college").toggle();
    $("#addCollege").prop("value", "Remove");
  }
  if ($("#postSchool").val().length > 0) {
    $("#post").toggle();
    $("#addPost").prop("value", "Remove");
  }
});

$("#addElem").click(function () {
  $("#elem").toggle();
  var str = $("#addElem").val();
  if (str.length === 3) {
    $("#addElem").prop("value", "Remove");
  } else {
    $("#addElem").prop("value", "Add");
    $("#elemSchool").removeAttr("value");
  }
});

$("#addJunior").click(function () {
  $("#junior").toggle();
  var str = $("#addJunior").val();
  if (str.length === 3) {
    $("#addJunior").prop("value", "Remove");
  } else {
    $("#addJunior").prop("value", "Add");
  }
});

$("#addSenior").click(function () {
  $("#senior").toggle();
  var str = $("#addSenior").val();
  if (str.length === 3) {
    $("#addSenior").prop("value", "Remove");
  } else {
    $("#addSenior").prop("value", "Add");
  }
});

$("#addCollege").click(function () {
  $("#college").toggle();
  var str = $("#addCollege").val();
  if (str.length === 3) {
    $("#addCollege").prop("value", "Remove");
  } else {
    $("#addCollege").prop("value", "Add");
  }
});

$("#addPost").click(function () {
  $("#post").toggle();
  var str = $("#addPost").val();
  if (str.length === 3) {
    $("#addPost").prop("value", "Remove");
  } else {
    $("#addPost").prop("value", "Add");
  }
});

$(function () {
  $("input[name='numonly']").on("input", function (e) {
    $(this).val(
      $(this)
        .val()
        .replace(/[^0-9]/g, "")
    );
  });
});

$(function () {
  $("#zipcode").change(function () {
    var max = parseInt($(this).attr("max"));
    var min = parseInt($(this).attr("min"));
    if ($(this).val() > max) {
      $(this).val(max);
    } else if ($(this).val() < min) {
      $(this).val(min);
    }
  });
});
$(function () {
  $("#height").change(function () {
    var max = parseInt($(this).attr("max"));
    var min = parseInt($(this).attr("min"));
    if ($(this).val() > max) {
      $(this).val(max);
    } else if ($(this).val() < min) {
      $(this).val(min);
    }
  });
});
$(function () {
  $("#weight").change(function () {
    var max = parseInt($(this).attr("max"));
    var min = parseInt($(this).attr("min"));
    if ($(this).val() > max) {
      $(this).val(max);
    } else if ($(this).val() < min) {
      $(this).val(min);
    }
  });
});
// var x = 1;
// $("#addTraining").click(function () {
//   $("#training").toggle();
//   var str = $("#addTraining").val();
//   console.log(str.length);
//   if (str.length === 3) {
//     $("#addTraining").prop("value", "Remove");
//   } else {
//     $("#addTraining").prop("value", "Add");
//   }
//   var str = "training-" + x;
//   x+= 1;
//   var html = '<div class="count "> <div class="d-flex justify-content-between"> <div class="flex">Training</div> <div class="flex"> <input type="button" value="Add" id="addTraining" class="btn ml-auto"style="background-color: #e94560; color: white" /> </div></div><div class="countID"><div class="form-row mt-4"> <div class="col-12 col-sm-6 mt-4 mt-sm-0"><input class="multisteps-form__input form-control" type="text" placeholder="Title" name="title" /> </div> <div class="col-12 col-sm-6 mt-4 mt-sm-0"> <input class="multisteps-form__input form-control" type="text" placeholder="Sponsor" name="sponsor" /> </div> </div> <div class="form-row mt-4"> <div class="col-12 col-sm-6 mt-4 mt-sm-0"> <input class="multisteps-form__input form-control" ="date" name="birthday" required /> </div> <div class="col-12 col-sm-6 mt-4 mt-sm-0"> <input class="multisteps-form__input form-control"type="venue"placeholder="Venue"name="venue"/></div></div></div></div><hr />';

// });

//profile
function triggerClick() {
  document.querySelector("#profileImage").click();
}
function displayImage(e) {
  if (e.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      document
        .querySelector("#profileDisplay")
        .setAttribute("src", e.target.result);
    };
    reader.readAsDataURL(e.files[0]);
  }
}
