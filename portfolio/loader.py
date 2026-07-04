# python portfolio/loader.py

import os
import json, uuid
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()


from portfolio.models import *

TFC.objects.all().delete()
Projeto.objects.all().delete()
UnidadeCurricular.objects.all().delete()

Tecnologia.objects.all().delete()
Aluno.objects.all().delete()
Professor.objects.all().delete()

Licenciatura.objects.all().delete()
Faculdade.objects.all().delete()


with open('portfolio/data/tfcs.json', encoding='utf-8') as f:
    tfcs = json.load(f)

    faculdade = Faculdade.objects.create(
        nome = "Universidade Lusófona",
        data_inauguracao = "1987-01-01",
        rua = "Rua Augusto Rosa",
        bairro = "Campo Grande",
        cidade = "Lisboa"
    )

    licenciatura = Licenciatura.objects.create(
        nome = "Engenharia Informática",
        ects = 180,
        descricao = "O curso de licenciatura em Engenharia Informática da Universidade Lusófona forma licenciados capazes de assumir posições de destaque em projetos de engenharia informática ou equipas de desenvolvimento e consultadoria, na área da engenharia dos sistemas de informação, assumindo pela sua formação e atitude papéis relevantes na geração de inovação e riqueza. Nesse sentido, os estudantes obtêm as competências adequadas à conceção, realização e manutenção de sistemas informáticos, programação de aplicações e de sistemas, desenho arquiteturas de computação e comunicações, gestão de sistemas de informação e de conhecimento, assim como à compreensão e resolução dos problemas associados.",
        objetivo_curso = "\n".join([
            "Aceder a um estatuto profissional com elevado potencial de mercado, através de um perfil reconhecido com fortes competências tecnológicas e humanas, garantindo um elevado grau de empregabilidade e a possibilidade de prosseguir os estudos de 2º ciclo com excelentes perspetivas de sucesso.",
            "Usufruir de um ensino de excelência assente num corpo docente de qualidade, integrando especialistas e doutorados com elevado potencial pedagógico e atividade comprovada em investigação.",
            "Ter acesso a vários estágios e formações empresariais ao longo do curso, no âmbito das diferentes parcerias desenvolvidas pelo DEISI, potenciando a empregabilidade assim como um nível de qualificação elevado antes da conclusão do curso.",
            "Poder efetuar o Trabalho Final de Curso inserido em projetos inovadores, pelo facto de uma maioria do seu corpo docente estar agregado aos Centros de Investigação da ECATI ou às empresas parceiras do DEISI.",
            "Tirar partido do Centro de Incubação de Empresas PLAY, que garante apoio às ideias dos jovens alunos mais empreendedores, potenciando a sua transformação em empresas de sucesso.",
            "Curso reconhecido pela Ordem dos Engenheiros Técnicos."
        ]),
        competencias_adquiridas = "\n".join([
            "O curso de licenciatura em Engenharia Informática da Universidade Lusófona desenvolve perfis com fortes competências tecnológicas e humanas, de forma a potenciar aos seus licenciados um elevado grau de empregabilidade, ou o prosseguimento dos estudos de 2º ciclo com excelentes perspectivas de sucesso. Os licenciados em Eng.ª Informática têm assim a possibilidade de escolher diversas carreiras profissionais:",
            "Analista Programador ",
            "Consultor na área das TI",
            "Arquitecto de Soluções",
            "Arquitecto/Administrador de Redes",
            "Nas seguintes áreas tecnológicas:",
            "Desenvolvimento de Aplicações Empresariais",
            "Desenvolvimento de Aplicações Móveis",
            "Concepção e Gestão de Repositórios de Informação",
            "Novos Paradigmas da Internet (Cloud Computing, Redes Sociais)",
            "Gestão de Sistemas Informáticos",
            "Etc..."
        ]),
        destinatario = "\n".join([
            "A Licenciatura em Engenharia Informática destina-se as estudantes que:",
            "Pretendam adquirir fortes competências em Tecnologias de Informação e Comunicação",
            "Procurem uma formação tecnológica avançada permanentemente adaptada à evolução das necessidades do mercado de trabalho, nas áreas de concepção, realização e manutenção de sistemas informáticos, programação de aplicações e de sistemas, desenho e arquitecturas de computação e comunicações e gestão de sistemas de informação;",
            "Pretendam desenvolver o espírito empreendedor, obtendo competências para criar conceitos originais e transformá-los em produtos inovadores. ",
            "Pretendam adquirir capacidade prosseguir os estudos de Mestrado, nomeadamente em Engenharia Informática e Sistemas de Informação e eventualmente escolher uma carreira académica.",
            "Para ingressar nesta Licenciatura, os candidatos deverão:",
            "Ser titulares de um curso de ensino secundário (12º ano) ou de habilitação legalmente equivalente e respectiva prova de acesso;",
            "Ter sido aprovados nas provas para Maiores de 23 anos."
        ]),
        ligacao_meio_empresarial = "\n".join([
            "O curso de licenciatura em Engenharia Informática da Universidade Lusófona pretende formar o perfil profissional do engenheiro de aplicações, caracterizado pela capacidade de participar em grandes projetos de engenharia informática, integrando equipas de desenvolvimento de projetos, gerindo e mantendo sistemas de informação. O diploma apresenta ainda uma formação aprofundadada em domínios comuns às Engenharias, como a Física e a Matemática, e em domínios específicos das Ciências Informáticas, como a Metodologia da Programação, os Sistemas de Informação, as Redes de Comunicações, e a gestão, tanto de sistemas como de projetos.",
            "Os Licenciados em Engenharia Informática encontrarão situações de emprego na rede Europeia de organismos públicos e privados com necessidades de desenvolvimento, utilização, reorganização e modernização de sistemas de informação, nomeadamente: ",
            "em empresas vocacionadas para o desenvolvimento e comercialização de soluções baseadas em informática; ",
            "na integração e chefia de equipas informáticas em grandes empresas dos setores comerciais, industriais ou dos serviços;",
            "em instituições ligadas ao setor público estatal ou privado, em particular na área dos serviços."
        ]),
        oportunidade_carreira = "\n".join([
            "Existem incentivos tendentes a estabelecer continuidade nos percursos académicos,  tais como a possibilidade aos alunos do 3º ano poderem obter ECTS do plano de estudos do Mestrado em Eng.ª Informática e Sistemas de Informação (MEISI) do mesmo Departamento, caso concluam o Trabalho Final de Curso (TFC) com bom aproveitamento e tiverem frequentado a cadeira de Seminário do Mestrado."
        ]),
        total_anos = 3,
        faculdade = faculdade
    )



    for info in tfcs:
        tfc = TFC.objects.create(
            titulo=info['titulo'],
            licenciatura=licenciatura,
            sumario=info.get('sumario', ''),
            link_pdf=info.get('link_pdf', ''),
            imagem=info.get('imagem', ''),
            palavras_chave=info.get('palavras_chave', ''),
            areas=info.get('areas', ''),
            rating=info.get('rating', 1)
        )

        autores = info.get('autores', '').split(';')
        for nome in autores:
            nome = nome.strip()
            if nome:
                aluno, _ = Aluno.objects.get_or_create(
                    nome=nome,
                    defaults={
                        "numero_aluno": str(uuid.uuid4())[:8],
                        "licenciatura": licenciatura
                    }
                )
                tfc.autores.add(aluno)

        orientadores = info.get('orientadores', '').split(';')
        for nome in orientadores:
            nome = nome.strip()
            if nome:
                prof, _ = Professor.objects.get_or_create(
                    nome=nome,
                    defaults={
                        "numero_professor": str(uuid.uuid4())[:8]
                    }
                )
                prof.licenciaturas.add(licenciatura)
                tfc.orientadores.add(prof)

        tecnologias = info.get('tecnologias_usadas', '').split(';')
        for nome in tecnologias:
            nome = nome.strip()
            if nome:
                tech, _ = Tecnologia.objects.get_or_create(
                    nome=nome,
                    defaults={
                        "link_website_oficial": "https://example.com"
                    }
                )
                tfc.tecnologias.add(tech)