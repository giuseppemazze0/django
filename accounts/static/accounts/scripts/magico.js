const inputEmail = document.querySelector("input[type='email']");
const link = document.querySelector(".link");

const gato = document.querySelector(".gato");
const gatoCima = document.querySelector(".gato-cima");
const gatoBaixo = document.querySelector(".gato-baixo");
const gatoEnviar = document.querySelector(".gato-enviar");

let cima = true;

const gatos = [
    gato,
    gatoCima,
    gatoBaixo,
    gatoEnviar
];

function mostrarGato(gatoMostrar) {
    gatos.forEach(gato => gato.classList.remove("mostrar"));

    gatoMostrar.classList.add("mostrar");
}



inputEmail.addEventListener("mouseenter", () => {
    mostrarGato(gatoCima)
});

inputEmail.addEventListener("focus", () => {
    mostrarGato(gatoCima)
});


inputEmail.addEventListener("keydown", () => {
    if (cima) {
        mostrarGato(gatoCima);
    } else {
        mostrarGato(gatoBaixo);
    }

    cima = !cima;
});


link.addEventListener("mouseenter", () => {
    mostrarGato(gatoEnviar)
});