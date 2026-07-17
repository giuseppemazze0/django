import './home.js';
import './resumo.js';

gsap.registerPlugin(ScrollSmoother);

const smoother = ScrollSmoother.create({
	smooth: 1, 
    smoothTouch: 0,
	effects: true	
});

document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();

        const target = document.querySelector(
            link.getAttribute('href')
        );

        smoother.scrollTo(target, true);
    });
});