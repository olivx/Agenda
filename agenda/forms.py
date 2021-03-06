from django import forms
from .models import Cadastro, Cidade


class CadastroForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        self.fields['cidade_fk'].queryset = Cidade.objects.none()

    class Meta:
        model = Cadastro
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'sobrenome': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'sexo': forms.Select(attrs={
                'class': 'custom-select form-control', }
            ),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'cargo': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
            }),
            'estado_fk': forms.Select(attrs={
                'class': 'custom-select form-control', }
            ),
            'cidade_fk': forms.Select(attrs={
                'class': 'custom-select form-control', }
            ),
        }
