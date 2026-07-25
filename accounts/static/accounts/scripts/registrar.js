const inputNome = document.querySelector("input[type='text']");
const inputSenhas = document.querySelectorAll("input[type='password']");
const inputEmail = document.querySelector("input[type='email']");
const linkRegistrar = document.querySelector(".link-registrar");

const gato = document.querySelector(".gato");
const gatoNome = document.querySelector(".gato-nome");
const gatoSenha = document.querySelector(".gato-senha");
const gatoConfirmar = document.querySelector(".gato-confirmar");
const gatoRegistrar = document.querySelector(".gato-registrar");
const gatoCima = document.querySelector(".gato-cima");
const gatoBaixo = document.querySelector(".gato-baixo");

let cima = true;

const gatos = [
    gato,
    gatoNome,
    gatoSenha,
    gatoConfirmar,
    gatoRegistrar,
    gatoCima,
    gatoBaixo,
];

function mostrarGato(gatoMostrar) {
    gatos.forEach(gato => gato.classList.remove("mostrar"));

    gatoMostrar.classList.add("mostrar");
}



inputNome.addEventListener("mouseenter", () => {
    mostrarGato(gatoNome)
});

inputNome.addEventListener("focus", () => {
    mostrarGato(gatoNome)
});


inputSenhas[0].addEventListener("mouseenter", () => {
    mostrarGato(gatoSenha)
});

inputSenhas[0].addEventListener("focus", () => {
    mostrarGato(gatoSenha)
});


inputSenhas[1].addEventListener("mouseenter", () => {
    mostrarGato(gatoConfirmar)
});

inputSenhas[1].addEventListener("focus", () => {
    mostrarGato(gatoConfirmar)
});


linkRegistrar.addEventListener("mouseenter", () => {
    mostrarGato(gatoRegistrar)
});



inputNome.addEventListener("mouseleave", () => {
    if (document.activeElement !== inputNome) {
        mostrarGato(gato);
    }
});

inputNome.addEventListener("blur", () => {
    mostrarGato(gato);
});


inputSenhas[0].addEventListener("mouseleave", () => {
    if (document.activeElement !== inputSenhas[0]) {
        mostrarGato(gato);
    }
});

inputSenhas[0].addEventListener("blur", () => {
    mostrarGato(gato);
});


inputSenhas[1].addEventListener("mouseleave", () => {
    if (document.activeElement !== inputSenhas[1]) {
        mostrarGato(gato);
    }
});

inputSenhas[1].addEventListener("blur", () => {
    mostrarGato(gato);
});


linkRegistrar.addEventListener("mouseleave", () => {
    mostrarGato(gato);
});







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

inputEmail.addEventListener("mouseleave", () => {
    if (document.activeElement !== inputEmail) {
        mostrarGato(gato);
    }
});

inputEmail.addEventListener("blur", () => {
    mostrarGato(gato);
});
