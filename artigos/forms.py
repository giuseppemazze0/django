from django import forms
from .models import Artigo, Comentario


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = [
            'titulo',
            'texto',
            'fotografia',
            'link_externo'
        ]

        error_messages = {
            "titulo": {
                "required": "*",
            },
            "texto": {
                "required": "*",
            },
            "fotografia": {
                "required": "*",
            },
            "link_externo": {
                "invalid": "Insira uma URL válida.",
            },
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario

        fields = ['texto']