from django.db import models


class Estado(models.Model):
    nom_estado = models.CharField(max_length=255)
    sgl_estado = models.CharField(max_length=2)

    class Meta:
        db_table = 'estado'

    def __str__(self):
        return self.nom_estado


class Cidade(models.Model):
    nom_cidade = models.CharField(max_length=255)
    cod_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        ordering = ('nom_cidade',)
        db_table = 'cidade'

    def __str__(self):
        return self.nom_cidade

class Cadastro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    email = models.EmailField(verbose_name="E-mail")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    celular = models.CharField(max_length=9, verbose_name="Celular")
    telefone = models.CharField(max_length=9, verbose_name="Tel.Fixo")
    SEXO = (
        ('HOMEM', 'Homem'),
        ('MULHER', 'Mulher'),
    )
    sexo = models.CharField(max_length=6, choices=SEXO)
    estado_fk = models.ForeignKey(Estado, on_delete=models.PROTECT,
                                  null=True, blank=True)
    cidade_fk = models.ForeignKey(Cidade, on_delete=models.PROTECT,
                                  null=True, blank=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'cadastro'
        verbose_name_plural = 'cadastros'

    def __str__(self):
        return self.nome

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'celular': self.celular,
        }
