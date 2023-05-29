let cantidadProducto = document.querySelector("#id_n_producto");
cantidadProducto.addEventListener('change', comprobarCantidad);

let botonAgregar = document.querySelector(".botonAgregar");
let errorCantidad = document.querySelector(".errorCantidad");


function comprobarCantidad(event) {
    let origen = event.currentTarget;
    let text = origen.value;

    if (text < 1) {
        respuesta = "La cantidad tiene que ser mayor que 0.";
  
        botonAgregar.disabled = true;
        botonAgregar.style.background = "gray";
        errorCantidad.style.display = "flex";
        origen.classList.add("imputIncorrecto");
      } else {
        botonAgregar.disabled = false;
        botonAgregar.style.background = "#3ba4c7";
        errorCantidad.style.display = "none";
        origen.classList.remove("imputIncorrecto");
      }
}
