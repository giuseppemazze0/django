const texto = document.querySelector(".texto");
const botao = document.querySelector(".lerMais");

botao.addEventListener("click", () => {
    texto.classList.toggle("expandido");

    if (texto.classList.contains("expandido")) {
        botao.textContent = "Ler menos";
    } else {
        botao.textContent = "Ler mais";
    }
});