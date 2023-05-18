// let cantidad = document.querySelector("#id_n_producto");
// cantidad.addEventListener("keyup", comprobarCantidad);

function comprobarCantidad(event) {

    let origen = event.currentTarget;
    let text = origen.value;

    if (text < 1) {
        respuesta = "La cantidad tiene que ser mayor que 0."
    }

    document.getElementById("informacionCantidad").textContent = respuesta
}

function Encima(event) {
    var origen = event.currentTarget;
    var filaCambiar = origen.querySelectorAll('td');
    filaCambiar.forEach(elem => elem.style.fontSize = '20px');
}
function Noencima(event) {
    var origen = event.currentTarget;
    var filaCambiar = origen.querySelectorAll('td');
    filaCambiar.forEach(elem => elem.style.fontSize = '14px');
}

let test =document.querySelectorAll("div.tablasList > table > tbody > tr");
var numTest = test.length;
for (var i = 0 ; i < test.length; i++) {
    test[i].addEventListener('mouseover', Encima);
}
let test1 = document.querySelectorAll('table tbody tr');
var numTest1 = test1.length;
for (var i = 0; i < test1.length; i++) {
    test1[i].addEventListener('mouseout', Noencima);
}

