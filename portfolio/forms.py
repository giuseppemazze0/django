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

        error_messages = {
            "nome": {
                "required": "*",
            },
            "logo": {
                "required": "*",
            },
            "link_website_oficial": {
                "required": "*",
            },
        }

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = "__all__"

        error_messages = {
            "nome": {
                "required": "*",
            },
            "nivel": {
                "required": "*",
            },
            "descricao": {
                "required": "*",
            },
        }

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'

        error_messages = {
            "nome": {
                "required": "*",
            },
            "instituicao": {
                "required": "*",
            },
            "data_inicio": {
                "required": "*",
            },
            "data_fim": {
                "required": "*",
            },
            "descricao": {
                "required": "*",
            },
             "competencias": {
                "required": "*",
            },
        }

        widgets = {
    "data_inicio": forms.DateInput(
        attrs={
            "type": "date",
            "placeholder": "xx/xx/xxxx",
        }
    ),
    "data_fim": forms.DateInput(
        attrs={
            "type": "date",
            "placeholder": "xx/xx/xxxx",
        }
    ),
}