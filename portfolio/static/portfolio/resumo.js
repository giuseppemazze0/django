gsap.registerPlugin(ScrollTrigger);


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