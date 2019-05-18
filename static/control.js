function setError() {
    $("#status").html('<span class="alert">Error</span>');
}

function turnXright() {
    $.get("/move/servoX/right", function(response) {
        $("#x").html(response);
    }).fail(function() {
        setError();
    });
}

function turnXleft() {
    $.get("/move/servoX/left", function(response) {
        $("#x").html(response);
    }).fail(function() {
        setError();
    });
}

function turnYright() {
    $.get("/move/servoY/right", function(response) {
        $("#y").html(response);
    }).fail(function() {
        setError();
    });
}

function turnYleft() {
    $.get("/move/servoY/left", function(response) {
        $("#y").html(response);
    }).fail(function() {
        setError();
    });
}

function sendText() {
    var toSay = $("#msg").val();
    $("#msg").val("");
    var data = { 'msg': toSay };
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

function saveScreenshot() {
    $.get("/save");
}

function load() {
    $.get("/pos/servoX", function(response) {
        $("#x").html(response);
    }).fail(function() {
        setError();
    });
    $.get("/pos/servoY", function(response) {
        $("#y").html(response);
    }).fail(function() {
        setError();
    });
}