from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        error_messages = {
            "nome": {
                "required": "*",
            },
            "ano_semestre": {
                "required": "*",
            },
            "descricao": {
                "required": "*",
            },
            "tecnologias": {
                "required": "*",
            },
            "link_github": {
                "required": "*",
            },
            "link_video": {
                "required": "*",
            },
            "uc": {
                "required": "*",
            },
            "imagem": {
                "required": "*",
            },
        }



class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'