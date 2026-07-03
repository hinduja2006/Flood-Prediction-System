// ================================
// Flood Prediction System
// main.js
// ================================

function validateForm() {

    const fields = document.querySelectorAll("input");

    for (let i = 0; i < fields.length; i++) {

        if (fields[i].value.trim() === "") {

            alert("Please fill all the fields.");

            fields[i].focus();

            return false;
        }

        if (parseFloat(fields[i].value) < 0) {

            alert("Values cannot be negative.");

            fields[i].focus();

            return false;
        }

    }

    return true;
}

// ================================
// Highlight Input on Focus
// ================================

document.addEventListener("DOMContentLoaded", function () {

    const inputs = document.querySelectorAll("input");

    inputs.forEach(function (input) {

        input.addEventListener("focus", function () {
            this.style.border = "2px solid #1565C0";
        });

        input.addEventListener("blur", function () {
            this.style.border = "1px solid #ccc";
        });

    });

});