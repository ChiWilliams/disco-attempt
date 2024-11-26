// static/script.js
function changeColor() {
    document.body.style.backgroundColor = 
        '#' + Math.floor(Math.random()*16777215).toString(16);
}


document.addEventListener("DOMContentLoaded", (e) => {
    document.getElementById("message").innerText = `hello from disco!!! the datetime is ${new Date()}`
});
