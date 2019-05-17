

function load() {
	var output = document.getElementById("x");
	output.innerHTML = 90;
}

function setError() {
  $("#status").html('<span class="alert">Error</span>');
}

function turnXright() {
  $.get("/servo/servoX/right", function(response) {
    $("#x").html(response);
  }).fail(function() {
    setError();
  });
}

function turnXleft() {
  $.get("/servo/servoX/left", function(response) {
    $("#x").html(response);
  }).fail(function() {
    setError();
  });
}

function turnYright() {
  $.get("/servo/servoY/right", function(response) {
    $("#y").html(response);
  }).fail(function() {
    setError();
  });
}

function turnYleft() {
  $.get("/servo/servoY/left", function(response) {
    $("#y").html(response);
  }).fail(function() {
    setError();
  });
}

function sendText() {
  var toSay = $("#msg").val();
  $("#msg").val("");
	var data = { 'msg' : toSay };
	$.ajax({
    type: 'POST',
    url: '/say',
		contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify(data)
  }).done(function(response) {
    $("#status").html(response);
	}).fail(function() {
    setError();
  });
}