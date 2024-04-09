const temperatureLabel = document.getElementById('temperatureValue');
const initialSeed = document.getElementById('initialSeed');
const temperature = document.getElementById('temperatureInput');
const steps = document.getElementById('stepsInput');
const left_container = document.querySelector('.left-container');
const socket = io('http://localhost:3000');
const sonnet = document.querySelector('.sonnet');
var cursor = document.querySelector('.cursor');



document.addEventListener('DOMContentLoaded', function () {
    temperatureLabel.textContent = temperature.value;
    temperature.addEventListener('input', function () {
        temperatureLabel.textContent = temperature.value;
    });
});

function isScrolledToBottom() {
    return window.innerHeight + window.scrollY >= document.body.scrollHeight - 20;
}

function updateUI(data) {
    data = data.replace(/\n/g, '<br>');
    cursor.insertAdjacentHTML('beforebegin', data);

    if (isScrolledToBottom) {
        window.scrollTo(0, document.body.scrollHeight);
    }
}
