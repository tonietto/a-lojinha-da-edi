from django.db import models
from django.core.validators import MinValueValidator
from django.utils.html import format_html

from decimal import Decimal


class CategoriaDaPeca(models.Model):
    categoria = models.CharField(max_length=30, unique=True)
    data_de_criacao = models.DateTimeField("criação", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.categoria

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "categoria__icontains",)

    class Meta:
        ordering = ('data_de_edicao',)
        verbose_name = 'categoria'


class CorDaPeca(models.Model):
    cor = models.CharField(max_length=30, unique=True)
    codigo = models.CharField("código",
                              max_length=7,
                              blank=True,
                              help_text='Código HEX da cor. Escolha em http://goo.gl/ZEQ38K. Ex.: #FFFFFF (Branco).')
    data_de_criacao = models.DateTimeField("criação", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.cor

    def circulo(self):
        return format_html('<svg height="12" width="12"><circle cx="6" cy="6" r="5" stroke="#efefef" stroke-width="1" fill="{0}" /></svg> ',
                           self.codigo)
    circulo.allow_tags = True

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "cor__icontains",)

    class Meta:
        ordering = ('data_de_edicao',)
        verbose_name = 'cor'
        verbose_name_plural = 'cores'


class TamanhoDaPeca(models.Model):
    tamanho = models.CharField(max_length=3, unique=True)
    data_de_criacao = models.DateTimeField("criação", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.tamanho

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "tamanho__icontains",)

    class Meta:
        ordering = ('data_de_edicao',)
        verbose_name = 'tamanho'


class TagsDaPeca(models.Model):
    tag = models.CharField(max_length=30, unique=True)
    data_de_criacao = models.DateTimeField("criação", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.tag

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "tag__icontains",)

    class Meta:
        ordering = ('data_de_edicao',)
        verbose_name_plural = 'tags das peças'


class Peca(models.Model):
    nome = models.CharField(max_length=60, default="")
    categoria = models.ForeignKey(CategoriaDaPeca)
    tags = models.ManyToManyField(TagsDaPeca, blank=True)
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
    referencia_original = models.CharField("referência original", max_length=30, blank=True, null=True)
    custo_unitario = models.DecimalField("custo R$",
                                         max_digits=5,
                                         decimal_places=2,
                                         default=Decimal('0.00'),
                                         validators=[MinValueValidator(Decimal('0.00'))])
    preco_unitario = models.DecimalField("preço R$",
                                         max_digits=5,
                                         decimal_places=2,
                                         default=Decimal('0.00'),
                                         validators=[MinValueValidator(Decimal('0.00'))])
    preco_unitario_promocional = models.DecimalField("promoção R$",
                                                     max_digits=5,
                                                     decimal_places=2,
                                                     validators=[MinValueValidator(Decimal('0.00'))],
                                                     blank=True, null=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.nome

    def thumbnail(self):
        return format_html('<div style="width: 30px; height: 30px; background-color: #fff; border-radius: 100px;"><img href="../../../{0}" style="width:100%;" ></div>',
                           self.imagem_1)
    thumbnail.short_description = 'Imagem'
    thumbnail.allow_tags = True

    def get_tags(self):
        return ", <br/>".join([p.tag for p in self.tags.all()[:5]])

    get_tags.short_description = 'tags'
    get_tags.allow_tags = True

    def get_cores(self):
        return ", <br/>".join([p.cor for p in self.cores.all()[:5]])

    get_cores.short_description = "cores"
    get_cores.allow_tags = True

    def lucro_unitario(self):
        if self.preco_unitario_promocional:
            calculo = self.preco_unitario_promocional - self.custo_unitario
        else:
            calculo = self.preco_unitario - self.custo_unitario
        return "R$%s" % calculo if calculo else ""

    lucro_unitario.short_description = 'lucro unit.'

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "nome__icontains",)

    class Meta:
        ordering = ('data_de_edicao',)
        verbose_name = 'peça'


class QuantidadeDePecasPorTamanho(models.Model):
    id_peca = models.ForeignKey(Peca)
    tamanho = models.ForeignKey(TamanhoDaPeca)
    data_de_criacao = models.DateTimeField("criação", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)
    """
    ex.: PPP, P, 36
    """
    quantidade_comprada = models.PositiveSmallIntegerField(default=0)
    quantidade_em_estoque = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.tamanho)

    class Meta:
        ordering = ('data_de_edicao',)
