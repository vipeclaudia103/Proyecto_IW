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

function pasarEncima(event) {
    var origen = event.currentTarget;
    var filaCambiar = origen.querySelectorAll('td');

}
function noPasarEncima(event) {
    var origen = event.currentTarget;
    var filaCambiar = origen.querySelectorAll('td');

}

let test = document.querySelectorAll("div.tablasList > table > tbody > tr");
var numTest = test.length;
for (var i = 0; i < test.length; i++) {
    test[i].addEventListener('mouseover', pasarEncima);
}
let test1 = document.querySelectorAll('table tbody tr');
var numTest1 = test1.length;
for (var i = 0; i < test1.length; i++) {
    test1[i].addEventListener('mouseout', noPasarEncima);
}
function activarMasInfo(event) {
    event.preventDefault();
    let origen = event.currentTarget;
    let idProducto = origen.parentElement.parentElement.id;
    let cuadContenido = document.querySelector('main')
    let cuadroDescripcion = document.createElement('div');
    fila.className = datos.length;
    borrar.className = 'content';
    borrar.textContent = 'Borrar';
    borrar.addEventListener("click", borrarElem);
    fila.append(borrar);
}

let btnInfo = document.querySelectorAll(".btnMasInfo");
for (var i = 0; i < test1.length; i++) {
    btnInfo[i].addEventListener("click", activarMasInfo);
}