function generateText() {
    var length = document.getElementById("length").value;
    var temperature = document.getElementById("temperature").value;

    console.log("Button clicked!");
    console.log("Sending request with length:", length, "and temperature:", temperature);

    fetch("https://6b83-34-75-206-44.ngrok-free.app/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "length": length,
            "temperature": temperature
        })
    })
    .then(response => {
        console.log("Got response:", response);
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }
        return response.json();
    })
    .then(data => {
        console.log("Received data:", data);
        document.getElementById("result").innerText = data.output;
        const resElement = document.querySelector('.res');
        resElement.innerHTML = resElement.innerText.replace(/\. /g, '.<br><br>');
    })
    .catch(error => {
        console.error("Error occurred:", error);
        document.getElementById("result").innerText = "An error occurred: " + error;
    });
}