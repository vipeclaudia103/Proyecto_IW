//ESTA EN emailCliente
let formu = document.getElementById("formularioComponente");
formu.addEventListener('submit', botonGuardar);

async function botonGuardar(event) {
    event.preventDefault();

    const data = new FormData(formu);
    response = await fetch('', {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        body: data
    }).then(function (response) {
        if (response.ok) {
            cuadroConfirmarAnadir();
        } else {
            throw "Error en la llamada Ajax";
        }
    });

};
async function cuadroConfirmarAnadir() {
    let cuadroAnadir = document.createElement('div');
    cuadroAnadir.className = 'anadirDiv';
    cuadroAnadir.id = 'cuadroAnadirId';
    let seleccionarSitio = document.getElementById("formularioComponentes");
    cuadroAnadir.innerHTML = "Añadido correctamente";
    seleccionarSitio.append(cuadroAnadir);
    setTimeout(cuadroConfirmarQuitar, 3000);

};

function cuadroConfirmarQuitar() {
    let selecciondivanadido = document.getElementsByClassName('anadirDiv');
    for (var i = 0; i < selecciondivanadido.length; i++) {
        selecciondivanadido[i].style.display = 'none';
    }
}



