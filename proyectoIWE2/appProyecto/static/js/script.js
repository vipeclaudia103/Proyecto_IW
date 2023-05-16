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