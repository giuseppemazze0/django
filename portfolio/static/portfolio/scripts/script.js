import './home.js';
import './resumo.js';

gsap.registerPlugin(ScrollSmoother);

const smoother = ScrollSmoother.create({
	smooth: 1, 
    smoothTouch: 0,
	effects: true	
});

const hamburguer = document.querySelector(".hamburguer");
const ul = document.querySelector("header nav ul");

const menuAberto = localStorage.getItem("menuAberto") === "true";

if (menuAberto) {
    ul.classList.add("mostrarMenu");
} else {
    ul.classList.remove("mostrarMenu");
    localStorage.setItem("menuAberto", ul.classList.contains("mostrarMenu"));
}

hamburguer.addEventListener("click", () => {
    ul.classList.toggle("mostrarMenu");
    localStorage.setItem("menuAberto", ul.classList.contains("mostrarMenu"));
});