<h1>Django</h1>
<br>

<h2>Informações úteis - Passo a Passo<h2>
<h3>Criar Aplicação</h3>
<p>python manage.py startapp [NOME]</p>
<p>Registrar no ficheiro settings.py na lista INSTALLED_APPS o nome da aplicação [NOME].</p>
<p>Criar os modelos em [NOME]/models.py</p>
<br>
<h3>Alterar ficheiro models.py da aplicação</h3>
<p>python manage.py makemigrations</p>
<p>python manage.py migrate</p>
<br>
<h3>Registrar os modelos em admin</h3>
<p>admin.site.register([NOME])</p>
<p>list_display, ordering, search_fields</p>
<br>
<h3>Correr o programa</h3>
<p>python manage.py runserver</p>
<br>

<h2>Informação do aluno</h2>
<p>Número do aluno: a22204542</p>
<p>Nome do aluno:   Giuseppe Mazzeo</p>
<br>
<br>

<h2>Credenciais de Superuser</h2>
<p>Username: admin</p>
<p>Password: admin</p>