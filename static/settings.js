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
    $.post("/settings", newConfig)
        .done(function() {
            alert("Settigns saved");
        })
        .fail(function() {
            alert("Could not save settings");
        });
}