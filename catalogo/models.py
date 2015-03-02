from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator


class CategoriaDaPeca(models.Model):
    categoria = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.categoria

    class Meta:
        ordering = ('categoria',)
        verbose_name = 'categoria'


class CorDaPeca(models.Model):
    cor = models.CharField(max_length=30, unique=True)
    codigo = models.CharField("código",
                              max_length=7,
                              blank=True,
                              help_text='Código HEX da cor. Escolha em http://goo.gl/ZEQ38K. Ex.: #FFFFFF (Branco).')

    def __str__(self):
        return self.cor

    class Meta:
        ordering = ('cor',)
        verbose_name = 'cor'
        verbose_name_plural = 'cores'


class TamanhoDaPeca(models.Model):
    tamanho = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.tamanho

    class Meta:
        ordering = ('tamanho',)
        verbose_name = 'tamanho'


class TagsDaPeca(models.Model):
    tag = models.CharField(max_length=30, unique=True)
    pub_date = models.DateTimeField("data de criação", auto_now_add=True)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ('pub_date', 'tag',)
        verbose_name = 'tag(s)'
        verbose_name_plural = 'tags'


class Peca(models.Model):
    nome = models.CharField(max_length=60, default="")
    categoria = models.ForeignKey(CategoriaDaPeca)
    """
    ex.: Blusa, Calça, Vestido
    """
    tags = models.ManyToManyField(TagsDaPeca, related_name='nome', blank=True)
    marca = models.ForeignKey('financeiro.Marca')
    cores = models.ManyToManyField(CorDaPeca, blank=True, null=True)
    GENERO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES,
                              default='F')
    imagem_1 = models.ImageField(upload_to='uploads/imagens/pecas/',
                                 blank=True)
    imagem_2 = models.ImageField(upload_to='uploads/imagens/pecas/',
                                 blank=True)
    imagem_3 = models.ImageField(upload_to='uploads/imagens/pecas/',
                                 blank=True)
    imagem_4 = models.ImageField(upload_to='uploads/imagens/pecas/',
                                 blank=True)
    mostrar_no_site = models.BooleanField(default=True)
    recibo = models.ForeignKey('financeiro.Recibo',
                               blank=True,
                               null=True)
    custo_unitario = models.DecimalField("custo",
                                         max_digits=5,
                                         decimal_places=2,
                                         default=Decimal('0.00'),
                                         validators=[MinValueValidator(Decimal('0.00'))])
    preco_unitario = models.DecimalField("preço",
                                         max_digits=5,
                                         decimal_places=2,
                                         default=Decimal('0.00'),
                                         validators=[MinValueValidator(Decimal('0.00'))])
    preco_unitario_promocional = models.DecimalField("preço promocional",
                                                     max_digits=5,
                                                     decimal_places=2,
                                                     default=Decimal('0.00'),
                                                     validators=[MinValueValidator(Decimal('0.00'))],
                                                     blank=True, null=True)
    pub_date = models.DateTimeField("data de publicacao", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('pub_date', 'nome')
        verbose_name = 'peça'


class QuantidadeDePecasPorTamanho(models.Model):
    peca = models.ForeignKey(Peca)
    tamanho = models.ForeignKey(TamanhoDaPeca)
    """
    ex.: PPP, P, 36
    """
    quantidade_comprada = models.PositiveSmallIntegerField(default=1)
    quantidade_em_estoque = models.PositiveSmallIntegerField(default=1)
