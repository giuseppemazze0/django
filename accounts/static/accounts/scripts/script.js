const inputNome = document.querySelector("input[type='text']");
const inputSenha = document.querySelector("input[type='password']");
const linkEntrar = document.querySelector(".link-entrar");
const linkMagico = document.querySelector(".link-magico");
const linkCriar = document.querySelector(".link-criar");

const gato = document.querySelector(".gato");
const gatoNome = document.querySelector(".gato-nome");
const gatoSenha = document.querySelector(".gato-senha");
const gatoEntrar = document.querySelector(".gato-entrar");
const gatoMagico = document.querySelector(".gato-magico");
const gatoCriar = document.querySelector(".gato-criar");

const gatos = [
    gato,
    gatoNome,
    gatoSenha,
    gatoEntrar,
    gatoMagico,
    gatoCriar
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


inputSenha.addEventListener("mouseenter", () => {
    mostrarGato(gatoSenha)
});

inputSenha.addEventListener("focus", () => {
    mostrarGato(gatoSenha)
});


linkEntrar.addEventListener("mouseenter", () => {
    mostrarGato(gatoEntrar)
});


linkMagico.addEventListener("mouseenter", () => {
    mostrarGato(gatoMagico)
});


linkCriar.addEventListener("mouseenter", () => {
    mostrarGato(gatoCriar)
});




inputNome.addEventListener("mouseleave", () => {
    if (document.activeElement !== inputNome) {
        mostrarGato(gato);
    }
});

inputNome.addEventListener("blur", () => {
    mostrarGato(gato);
});


inputSenha.addEventListener("mouseleave", () => {
    if (document.activeElement !== inputSenha) {
        mostrarGato(gato);
    }
});

inputSenha.addEventListener("blur", () => {
    mostrarGato(gato);
});


linkEntrar.addEventListener("mouseleave", () => {
    mostrarGato(gato);
});


linkMagico.addEventListener("mouseleave", () => {
    mostrarGato(gato);
});


linkCriar.addEventListener("mouseleave", () => {
    mostrarGato(gato);
});