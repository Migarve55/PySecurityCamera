function saveConfig() {
    let newConfig = {
        "camera": {
            "servo": {
                "pan": {
                    "step": $("#stepX").val(),
                    "min": $("#minX").val(),
                    "max": $("#maxX").val()
                },
                "tilt": {
                    "step": $("#stepY").val(),
                    "min": $("#minY").val(),
                    "max": $("#maxY").val()
                }
            },
            "speech": {
                "voice": $("#voice").val(),
                "rate": $("#rate").val()
            }
        }
    };
    $.ajax({
        type: "POST",
        url: "/settings",
        dataType: "json",
        success: function(msg) {
            console.log("saved: " + msg);
        },
        fail: function() {
            alert("Could not save settings!!!");
        },
        data: newConfig
    });

}