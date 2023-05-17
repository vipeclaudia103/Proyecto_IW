let cantidad = document.querySelector("#id_n_producto");
cantidad.addEventListener("keyup", comprobarCantidad);

function comprobarCantidad(event) {

    let origen = event.currentTarget;
    let text = origen.value;

    if (text < 1) {
        respuesta = "La cantidad tiene que ser mayor que 0."
    }

    document.getElementById("informacionCantidad").textContent = respuesta
}

function Encima(event){
    event.target.style.fontSize = '30px';
}
function Noencima(event){
    event.target.style.fontSize = '14px';
}

let test = document.querySelectorAll('table.listados tbody tr');
var numTest = test.length;
for (var i = 0 ; i < test.length; i++) {
    var a =test[i].addEventListener('mouseover', Encima);
}
let test1 = document.querySelectorAll('table.listados tbody tr');
var numTest1 = test1.length;
for (var i = 0 ; i < test1.length; i++) {
    test1[i].addEventListener('mouseout', Noencima);
}

