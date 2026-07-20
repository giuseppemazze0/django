gsap.registerPlugin(ScrollTrigger);

const projetos = document.querySelectorAll('.projeto');
let x = 0;

for (let i = 1; i < projetos.length; i++) {
    x = (i % 2 == 0) ? -80 : 80;
    gsap.from(projetos[i], {
        opacity: 0,
        x: x,
        duration: 1,
        scrollTrigger: {
            trigger: projetos[i],
            start: `top 50%`,
        }
    });
}

gsap.from(projeto[0], {
    opacity: 0,
    x: -60,
    scrollTrigger: {
        trigger: '.main-projetos',
        start: `top top`,
        markers: true
    }
});