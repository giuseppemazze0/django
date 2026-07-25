from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistoForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "Nome de utilizador"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "E-mail"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "placeholder": "Nome de utilizador"
        })

        self.fields["email"].widget.attrs.update({
            "placeholder": "E-mail"
        })

        self.fields["password1"].widget.attrs.update({
            "placeholder": "Palavra-passe"
        })

        self.fields["password2"].widget.attrs.update({
            "placeholder": "Confirmar palavra-passe"
        })