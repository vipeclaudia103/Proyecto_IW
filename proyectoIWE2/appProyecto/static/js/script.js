let textoModo = document.querySelector("#modoPagina");
var linkElement = document.getElementById("estilos");


// Obtener el botón y asignarle el evento de clic
let modoOscuro = document.querySelector("#modoOscuro");
let modoClaro = document.querySelector("#modoClaro");
modoOscuro.addEventListener("click", cambiarEstiloOscuro);
modoClaro.addEventListener("click", cambiarEstiloClaro);
// Set a Cookie
function setCookie(cName, cValue, expDays) {
    let date = new Date();
    date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = cName + "=" + cValue + "; " + expires + "; path=/appProyecto";
}
function getCookie(cName) {
    const name = cName + "=";
    const cDecoded = decodeURIComponent(document.cookie); //to be careful
    const cArr = cDecoded.split('; ');
    let res;
    cArr.forEach(val => {
        if (val.indexOf(name) === 0) res = val.substring(name.length);
    })
    return res;
}
document.addEventListener('DOMContentLoaded', function () {
    var estadoGuardado = localStorage.getItem("estadoEstilo");
    if ((getCookie('rutaCSS') === "claro") && (estadoGuardado === "alternativo")) {
        cambiarEstiloClaro();
    } else {
        cambiarEstiloOscuro();
    }
});

function setModo(modo) {
    document.cookie = "rutaCSS=" + encodeURIComponent(modo);
    console.log(modo);
    setCookie('rutaCSS', modo, 30);
}

// Función para cambiar el estilo a Estilo Original
function cambiarEstiloClaro() {

    modoClaro.style.display = 'none';
    linkElement.href = "http://127.0.0.1:8000/static/css/estilosClaros.css";
    textoModo.textContent = "CLARO"
    modoOscuro.style.display = "block";
    localStorage.setItem("estadoEstilo", "alternativo");
    localStorage.setItem("rutaCSS", linkElement.href);
    setModo("claro");
}

// Función para cambiar el estilo a Estilo Alternativo
function cambiarEstiloOscuro() {
    linkElement.href = "http://127.0.0.1:8000/static/css/estilos.css";
    textoModo.textContent = "OSCURO"
    modoClaro.style.display = "block";
    modoOscuro.style.display = "none";
    localStorage.setItem("estadoEstilo", "original");
    localStorage.setItem("rutaCSS", linkElement.href);
    setModo("oscuro");

}



