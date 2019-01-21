from django import forms
from .models import Cadastro, Cidade


class CadastroForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        self.fields['cidade_fk'].queryset = Cidade.objects.none()

        # hack para funcionar com modelform
        if 'estado_fk' in self.data:
            try:
                estado_fk = int(self.data.get('estado_fk'))
                self.fields['cidade_fk'].queryset = Cidade.objects.filter(cod_estado=estado_fk).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['cidade_fk'].queryset = self.instance.estado_fk.cidade_fk_set.order_by('name')

    class Meta:
        model = Cadastro
        fields = ('nome', 'sobrenome', 'email', 'endereco', 'sexo', 'telefone', 'celular',
                  'cargo', 'estado_fk', 'cidade_fk')
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

