let correoCliente = document.querySelector("#btnCorreoCliente");
let div = document.querySelector(".contactoCliente");
correoCliente.addEventListener("click", mostrarFormulario);
let btnCerrar = document.querySelector(".botonCerrar");
btnCerrar.addEventListener("click", cerrar);
let idCorreo = document.querySelector("#idCorreo");

function mostrarFormulario() {
    div.style.display = "flex";
    let correo = document.querySelector("#correoCliente");
    idCorreo.value = correo.textContent;
}

function cerrar() {
    div.style.display = "none";
}
