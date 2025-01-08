function predictPrice() {
    var form = document.getElementById("inputForm");
    var formData = new FormData(form);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/predict", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById("output").innerHTML = "Predicted Price: $" + response.predicted_price;
        }
    };
    xhr.send(formData);
}
