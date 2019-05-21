function setStatus(msg) {
    $("#status").html(msg);
}

function saveConfig() {
    let newConfig = {
        servo: {
            pan: {
                step: $("#stepX").val(),
                min: $("#minX").val(),
                max: $("#maxX").val()
            },
            tilt: {
                step: $("#stepY").val(),
                min: $("#minY").val(),
                max: $("#maxY").val()
            }
        },
        speech: {
            voice: $("#voice").val(),
            rate: $("#rate").val()
        }
    };
    $.ajax({
        type: 'POST',
        url: '/settings',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(newConfig)
    }).done(function(response) {
        setStatus("Saved");
    }).fail(function() {
        setStatus("Error");
    });
}