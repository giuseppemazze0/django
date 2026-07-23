gsap.registerPlugin(ScrollTrigger);

const tl = gsap.timeline({delay: .4});
const titulos = document.querySelectorAll('.tituloEfeito');

titulos.forEach(titulo => {
    const texto = titulo.textContent;
    const letras = texto.split('');

    titulo.textContent = '';

    letras.forEach(letra => {
        const span = document.createElement('span');
        span.textContent = letra;
        titulo.appendChild(span);
    });

    tl.from(titulo.children, {
        opacity: 0,
        y: 60,
        stagger: .08,
        duration: 0.2,
        ease: "power1.out"
    });
});



tl.from('.li-menu', {
    opacity: 0,
    y: -40,
    stagger: .1
}, '-=.2')

.from('.li-rs', {
    opacity: 0,
    y: -40,
    stagger: .1
}, '<')

.from('.li-descricao', {
    opacity: 0,
    x: -50,
    stagger: .1
}, '-=.1')

.from('#home .botoes button', {
    opacity: 0,
    y: 40
}, '-=.1')

.fromTo('.pessoa', {
    opacity: 0,
    x: 80
}, {
    opacity: 1,
    x: 0
});






gsap.from('.educacao', {
    opacity: 0,
    x: 40,
    scrollTrigger: {
        trigger: '#resumo',
        start: '-10% 20%',
        end: '+=80',
        scrub: 1
    }
});

gsap.from('.interesses', {
    opacity: 0,
    x: -40,
    scrollTrigger: {
        trigger: '#resumo',
        start: '0% 20%',
        end: '+=80',
        scrub: 1
    }
});

gsap.from('.linguas', {
    opacity: 0,
    x: -40,
    scrollTrigger: {
        trigger: '#resumo',
        start: '0% 20%',
        end: '+=80',
        scrub: 1
    }
});

gsap.from('.experienciaProfissional', {
    opacity: 0,
    x: 40,
    scrollTrigger: {
        trigger: '#resumo',
        start: '10% 20%',
        end: '+=80',
        scrub: 1
    }
});

gsap.from('.ferramentas', {
    opacity: 0,
    y: 40,
    scrollTrigger: {
        trigger: '#resumo',
        start: '17% 20%',
        end: '+=100',
        scrub: 1,
    }
});