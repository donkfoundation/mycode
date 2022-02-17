let body = document.querySelector('body');

document.querySelector('#green').addEventListener('click', function() {
    body.style.backgroundColor = 'green';
});
document.querySelector('#red').addEventListener('click', function() {
    body.style.backgroundColor = 'red';
});
document.querySelector('#blue').addEventListener('click', function() {
    body.style.backgroundColor = 'blue';
});

var hovers = 0

document.querySelector("#second").addEventListener('mouseover', function () {
    hovers++;
    console.log(hovers)
    if (hovers % 5 == 0) {
        alert("Stop")
    };
});

function funcion() {
    var nombre = document.getElementById("SquareName").value; 
    document.getElementById("paragraph").innerHTML = nombre;
}; 
