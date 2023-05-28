const urlActual = window.location.href;
if (urlActual.includes("productos")) {

  let cantidadProducto = document.querySelector("#id_cantidad");
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

      origen.style.borderColor = "red";

      errorCantidad.style.display = "flex";
      
    } else {
      botonAgregar.disabled = false;
      botonAgregar.style.background = "#3ba4c7";

      errorCantidad.style.display = "none";
    }
  }
}
