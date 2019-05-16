
function load() {
	var output = document.getElementById("x");
	output.innerHTML = 90;
}

function makeHttpObject() {
  try {return new XMLHttpRequest();}
  catch (error) {}
  try {return new ActiveXObject("Msxml2.XMLHTTP");}
  catch (error) {}
  try {return new ActiveXObject("Microsoft.XMLHTTP");}
  catch (error) {}

  throw new Error("Could not create HTTP request object.");
}

function turnYright() {
  var request = makeHttpObject();
  request.open("GET", "http://mgvhome.duckdns.org:56082/servo/servoY/right", true);
  request.send();
  var output = document.getElementById("x");
  output.innerHTML = request.responseText;
}

function turnYleft() {
  var request = makeHttpObject();
  request.open("GET", "http://mgvhome.duckdns.org:56082/servo/servoY/left", true);
  request.send();
  var output = document.getElementById("x");
  output.innerHTML = request.responseText;
}

function sendText() {
    var toSay = document.getElementById("msg").value;
	var data = { 'msg' : toSay };
	$.ajax({
        type: 'POST',
        url: '/say',
		contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(data)
    }).done(function(response) {
		document.getElementById("status").innerHTML = response;
	});
}