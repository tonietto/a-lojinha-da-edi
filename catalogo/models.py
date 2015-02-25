from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator


class CategoriaDaPeca(models.Model):
    categoria = models.CharField(max_length=30, unique=True, default="Nenhuma")

    def __str__(self):
        return self.categoria

    class Meta:
        ordering = ('categoria',)
        verbose_name = 'categoria'


class CorDaPeca(models.Model):
    cor = models.CharField(max_length=30, unique=True, default="Branca")
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
    tamanho = models.CharField(max_length=3, unique=True, default="M")

    def __str__(self):
        return self.tamanho

    class Meta:
        ordering = ('tamanho',)
        verbose_name = 'tamanho'


class TagsDaPeca(models.Model):
    tag = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(help_text='URL da tag. Ex.: manga-longa')
    pub_date = models.DateTimeField("data de criação", auto_now_add=True)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ('pub_date', 'tag',)
        verbose_name = 'tag(s)'
        verbose_name_plural = 'tags'


class Peca(models.Model):
    nome = models.CharField(max_length=30, default="")
    categoria = models.ForeignKey(CategoriaDaPeca)
    """
    ex.: Blusa, Calça, Vestido
    """
    slug = models.SlugField(help_text='URL. Ex.: blusinha-guardachuvas')
    tags = models.ManyToManyField(TagsDaPeca, related_name='nome')
    marca = models.ForeignKey('financeiro.Marca')
    cor = models.ForeignKey(CorDaPeca, blank=True, null=True)
    tamanho = models.ForeignKey(TamanhoDaPeca)
    """
    ex.: PPP, P, 36
    """
    GENERO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES,
                              default='F')
    imagem_1 = models.ImageField(upload_to='imagem_do_produto',
                                 blank=False)
    imagem_2 = models.ImageField(upload_to='imagem_do_produto',
                                 blank=True)
    imagem_3 = models.ImageField(upload_to='imagem_do_produto',
                                 blank=True)
    imagem_4 = models.ImageField(upload_to='foto_do_produto',
                                 blank=True)
    ativa = models.BooleanField("ativa no site", default=True)
    quantidade_comprada = models.PositiveSmallIntegerField(default=1)
    quantidade_em_estoque = models.PositiveSmallIntegerField(default=1)
    reservada = models.BooleanField(default=False)
    nota_fiscal = models.ForeignKey('financeiro.NotaFiscal',
                                    blank=True,
                                    null=True)
    venda = models.ForeignKey('financeiro.Venda',
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
                                                     validators=[MinValueValidator(Decimal('0.00'))])
    valor_venda = models.DecimalField("valor venda", max_digits=5,
                                      decimal_places=2,
                                      blank=True, null=True)
    pub_date = models.DateTimeField("data de publicacao", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('pub_date', 'nome')
        verbose_name = 'peça'
