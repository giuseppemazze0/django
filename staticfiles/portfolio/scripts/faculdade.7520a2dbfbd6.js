gsap.from('.menu-cards > .card', {
    opacity: 0,
    y: 40,
    stagger: .3,
    delay: .4,
});


gsap.from('.destaque', {
    opacity: 0,
    y: -40,
    scrollTrigger: {
        trigger: "#quem-somos",
        start: "bottom 50%"
    }
});


const cards = gsap.utils.toArray(".card-legal");
let delay = .1;

for (let card of cards) {
    gsap.from(card, {
        opacity: 0,
        y: 40,
        delay: delay,
        ease: "power2.out",
        scrollTrigger: {
            trigger: "#licenciatura",
            start: "top 50%",
        }
    });
    delay += .1;
}

gsap.from("#licenciatura h3", {
    opacity: 0,
    x: -40,
    ease: "power2.out",
    scrollTrigger: {
        trigger: "#licenciatura",
        start: "top 50%",
    }
});
