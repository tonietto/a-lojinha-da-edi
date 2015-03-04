from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    telefone = models.PositiveSmallIntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to='foto_do_cliente', blank=True)
    cidade = models.ForeignKey('financeiro.Cidade', blank=True)
    rua = models.CharField(max_length=150, blank=True)
    numero = models.PositiveSmallIntegerField("número", blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True)
    anotacoes = models.TextField("anotações", blank=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('data_de_edicao', 'nome')
