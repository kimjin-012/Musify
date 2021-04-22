$(".main-btn").click(function () {
    $(".search-description").slideToggle(100);
});
$(".search-description li").click(function () {
    var target = $(this).html();
    var toRemove = "By ";
    var newTarget = target.replace(toRemove, "");
  //remove spaces
    newTarget = newTarget.replace(/\s/g, "");
    $(".search-large").html(newTarget);
    $(".search-description").hide();
    $(".main-input").hide();
    newTarget = newTarget.toLowerCase();
    $(".main-" + newTarget).show();
});
$("#main-submit-mobile").click(function () {
    $("#main-submit").trigger("click");
});
$(window).resize(function () {
    replaceMatches();
});

function replaceMatches() {
    var width = $(window).width();
    if (width < 516) {
        $(".main-title").attr("value", "Search by Title");
    } else {
        $(".main-artist").attr("value", "Search by Artist Name");
    }
}
replaceMatches();

function clearText(thefield) {
    if (thefield.defaultValue == thefield.value) {
    thefield.value = "";
    }
}

function replaceText(thefield) {
    if (thefield.value == "") {
    thefield.value = thefield.defaultValue;
    }
}

Resources;
