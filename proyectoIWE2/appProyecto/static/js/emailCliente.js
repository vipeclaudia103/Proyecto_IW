let correoCliente = document.querySelector("#correoCliente");
let div = document.querySelector(".contactoCliente");
correoCliente.addEventListener("click", mostrarFormulario);
let btnCerrar = document.querySelector(".botonCerrar");
btnCerrar.addEventListener("click", cerrar);
let idCorreo = document.querySelector("#idCorreo");

function mostrarFormulario(event) {
    div.style.display = "flex";
    idCorreo.value = correoCliente.textContent;
}

function cerrar(event) {
    div.style.display = "none";
}
