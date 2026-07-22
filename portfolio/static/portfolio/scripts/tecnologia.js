gsap.registerPlugin(ScrollTrigger);

const container = document.querySelector(".tecnologias");
const todosCards = [];

function criarHtml(tecnologia) {
    const divTec = document.createElement("div");
    divTec.classList.add("tecnologia");

    const card = document.createElement("div");
    card.classList.add("card");

    const link = document.createElement("a");
    link.href = tecnologia.website;
    link.target = "_blank";

    const icone = document.createElement("i");
    icone.classList.add("fi", "fi-bs-up-right-from-square");

    if (tecnologia.logo) {
        const imagem = document.createElement("img");
        imagem.src = tecnologia.logo;
        imagem.alt = tecnologia.nome;
        card.appendChild(imagem);
    } else {
        const placeholder = document.createElement("i");
        placeholder.className = "fi fi-rr-picture";
        card.appendChild(placeholder);
    }

    const titulo = document.createElement("h3");
    titulo.textContent = tecnologia.nome;

    link.appendChild(icone);

    card.appendChild(link);
    card.appendChild(titulo);


    divTec.appendChild(card);

    todosCards.push(divTec);
}


function separarCards() {
    const superior = document.querySelector(".superior");
    const inferior = document.querySelector(".inferior");
    const inf = [];

    for (let i = 0; i < todosCards.length; i++) {
        if (i % 2 == 0) {
            superior.appendChild(todosCards[i]);
        } else {
            inf.push(todosCards[i]);
        }
    }

    inf.reverse().forEach(card => inferior.appendChild(card));

    definirGsap();
}


function definirGsap() {
    const superior = document.querySelector(".superior");
    const inferior = document.querySelector(".inferior");
    const card = document.querySelector('.tecnologia');

    const maiorLinha = superior.scrollWidth > inferior.scrollWidth ? superior : inferior;

    const scrollDistance = maiorLinha.scrollWidth - container.clientWidth + card.offsetWidth;

    gsap.set(inferior, {
        x: -(scrollDistance - 140)
    });

    const tl = gsap.timeline({
        scrollTrigger: {
            trigger: container,
            start: "top top",
            end: `+=${scrollDistance}`,
            scrub: 1,
            pin: true,
        }
    });

    tl.to(superior, {
        x: -scrollDistance,
        ease: "none"
    }, 0);

    tl.to(inferior, {
        x: 160,
        ease: "none"
    }, 0);
}



for (const tecnologia of tecnologias) {
    criarHtml(tecnologia);
}

separarCards();