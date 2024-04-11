document.addEventListener('DOMContentLoaded', (event) => {
    let startBtn = document.getElementById('start');
    let stopBtn = document.getElementById('stop');
    let resetBtn = document.getElementById('reset');
    let secElement = document.getElementById('sec');
    let tpmElement = document.getElementById('tpm');

    let seconds = 0;
    let tpm = 0;
    let intervalId = null;

    startBtn.addEventListener('click', function () {
        // Clear any existing interval
        if (intervalId !== null) {
            clearInterval(intervalId);
        }

        // Start a new interval
        intervalId = setInterval(function () {
            seconds++;
            tpm = seconds > 0 ? 60 / seconds : 0;

            // Update the displayed time and count
            secElement.textContent = pad(seconds, 2);
            tpmElement.textContent = tpm;
        }, 1000);
    });

    stopBtn.addEventListener('click', function () {
        // Stop the interval
        if (intervalId !== null) {
            clearInterval(intervalId);
        }
    });

    resetBtn.addEventListener('click', function () {
        // Stop the interval and reset the time and count
        if (intervalId !== null) {
            clearInterval(intervalId);
        }
        seconds = 0;
        tpm = 0;
        secElement.textContent = '00';
        tpmElement.textContent = '0';
    });
});

// Function to pad a number with leading zeros
function pad(num, size) {
    let s = num + "";
    while (s.length < size) s = "0" + s;
    return s;
}