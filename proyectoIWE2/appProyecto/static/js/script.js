const API = {
    SERVICE_URL: "http://127.0.0.1:8000/appProyecto",
    Producto: "/productos/",
    Pedidos: "/pedidos/",
    Clientes: "/clientes/",
    Componentes: "/componentes/",
    Categoria: "/categoria/"
}
    
let cantidadProducto = document.querySelector("#id_n_producto");
cantidadProducto.addEventListener("keyup", comprobarCantidad);
function comprobarCantidad(event) {
  let origen = event.currentTarget;
  let text = origen.value;

  let botonAgregar = document.querySelector(".botonAgregar");
  let errorCantidad = document.querySelector("#errorCantidad");

  if (text < 1) {
    respuesta = "La cantidad tiene que ser mayor que 0.";

    botonAgregar.disabled = true;
    botonAgregar.style.background = "gray";

    origen.style.borderColor = "red";
  } else {
    botonAgregar.disabled = false;
    botonAgregar.style.background = "#3ba4c7";
    origen.border;
  }

  document.getElementById("informacionCantidad").textContent = respuesta;
}







// function pasarEncima(event) {
//     var origen = event.currentTarget;
//     var filaCambiar = origen.querySelectorAll('td');

// }
// function noPasarEncima(event) {
//     var origen = event.currentTarget;
//     var filaCambiar = origen.querySelectorAll('td');

// }

// let test = document.querySelectorAll("div.tablasList > table > tbody > tr");
// var numTest = test.length;
// for (var i = 0; i < test.length; i++) {
//     test[i].addEventListener('mouseover', pasarEncima);
// }
// let test1 = document.querySelectorAll('table tbody tr');
// var numTest1 = test1.length;
// for (var i = 0; i < test1.length; i++) {
//     test1[i].addEventListener('mouseout', noPasarEncima);
// }