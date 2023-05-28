let cuadContenido = document.querySelector('#cuadroInformacion')

function activarMasInfo(event) {
    event.preventDefault();

    let origen = event.currentTarget;
    let cuadroDescripcion = document.createElement('div');
    cuadContenido.className = 'content'
    let descrip = origen.parentElement.parentElement.querySelector(".complete");
    origen.style.display = 'none';
    let menos = origen.parentElement.querySelector("a.btnMenosInfo");
    menos.style.display = 'inline';
    cuadContenido.innerHTML = '<h2> Descripcion</h2>   <div class="contenidoMasInfo">' + descrip.textContent + '</div>';
    cuadroDescripcion.innerHTML = '';
    cuadContenido.append(cuadroDescripcion);
    cuadContenido.style.display = 'block';

}
function btnInfoMenosElem(event) {
    let origen = event.currentTarget;
    let mas = origen.parentElement.querySelector(".btnMasInfo");
    let menos = origen.parentElement.querySelector(".btnMenosInfo");
    cuadContenido.innerHTML = '';
    cuadContenido.className = '';
    menos.style.display = 'none';
    mas.style.display = 'inline';
}

let btnInfo = document.querySelectorAll(".btnMasInfo");
let btnMenosInfo = document.querySelectorAll(".btnMenosInfo");
for (var i = 0; i < btnInfo.length; i++) {
    btnInfo[i].addEventListener("click", activarMasInfo);
    btnMenosInfo[i].addEventListener("click", btnInfoMenosElem);
}
if (cuadContenido.style.display == "none") {
    for (var i = 0; i < btnInfo.length; i++) {
        btnInfo[i].style.display = "inline";
        btnMenosInfo[i].style.display = "none";
    }
}