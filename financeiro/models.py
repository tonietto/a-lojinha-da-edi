from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.utils import timezone


NOTA_CHOICES = (
    ('0', 'Péssimo'),
    ('1', 'Regular'),
    ('2', 'Bom'),
    ('3', 'Ótimo'),
)


agora = timezone.now()


class Cidade(models.Model):
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2, help_text="Sigla do Estado.")
    pais = models.CharField("país", max_length=30, default="Brasil")
    anotacoes = models.TextField("anotações", blank=True)
    pub_date = models.DateTimeField("data de cadastro", auto_now_add=True)


class Shopping(models.Model):
    nome = models.CharField(max_length=30)
    cidade = models.ForeignKey(Cidade)
    rua = models.CharField(max_length=150, blank=True)
    numero = models.PositiveSmallIntegerField("número", blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True)
    nota = models.CharField(max_length=1, choices=NOTA_CHOICES, default=1)
    anotacoes = models.TextField("anotações", blank=True)
    pub_date = models.DateTimeField("data de cadastro", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome', 'pub_date')


class Guia(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30, blank=True)
    cidade = models.ForeignKey(Cidade)
    email = models.EmailField(max_length=254, blank=True)
    telefone = models.PositiveSmallIntegerField(blank=True, null=True)
    shoppings = models.ManyToManyField(Shopping)
    nota = models.CharField(max_length=1, choices=NOTA_CHOICES, default=1)
    anotacoes = models.TextField("anotações", blank=True)
    pub_date = models.DateTimeField("data de cadastro", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome', 'pub_date')


class Loja(models.Model):
    nome = models.CharField(max_length=30)
    LOJA_CHOICES = (
        ('R', 'Loja de Rua'),
        ('S', 'Loja de Shopping'),
    )
    tipo_de_loja = models.CharField(max_length=1,
                                    choices=LOJA_CHOICES,
                                    default=2)
    shopping = models.ForeignKey(Shopping,
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL)
    cnpj = models.PositiveSmallIntegerField("CNPJ", blank=True, null=True)
    cidade = models.ForeignKey(Cidade)
    email = models.EmailField(max_length=254, blank=True)
    telefone = models.PositiveSmallIntegerField(blank=True, null=True)
    nota = models.CharField(max_length=1, choices=NOTA_CHOICES, default=1)
    anotacoes = models.TextField("anotações", blank=True)
    pub_date = models.DateTimeField("data de cadastro", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome', 'pub_date')


class Marca(models.Model):
    nome = models.CharField(max_length=30)
    nota = models.CharField(max_length=1, choices=NOTA_CHOICES, default=1)
    anotacoes = models.TextField("anotações", blank=True)
    imagem = models.ImageField(upload_to='imagem_da_marca', blank=True)
    pub_date = models.DateTimeField("data de cadastro", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome', 'pub_date')


class Viagem(models.Model):
    nome = models.CharField(max_length=150)
    data_da_viagem = models.DateField(default=agora)
    cidade = models.ForeignKey(Cidade)
    custo_combustivel = models.DecimalField("combustível",
                                            max_digits=5,
                                            decimal_places=2,
                                            default=Decimal('0.00'),
                                            validators=[MinValueValidator(Decimal('0.00'))])
    custo_pedagios = models.DecimalField("pedágios",
                                         max_digits=5,
                                         decimal_places=2,
                                         default=Decimal('0.00'),
                                         validators=[MinValueValidator(Decimal('0.00'))])
    custo_alimentacao = models.DecimalField("alimentação",
                                            max_digits=5,
                                            decimal_places=2,
                                            default=Decimal('0.00'),
                                            validators=[MinValueValidator(Decimal('0.00'))])
    custo_estacionamento = models.DecimalField("estacionamento",
                                               max_digits=5,
                                               decimal_places=2,
                                               default=Decimal('0.00'),
                                               validators=[MinValueValidator(Decimal('0.00'))])
    custo_transporte = models.DecimalField("transporte",
                                           max_digits=5,
                                           decimal_places=2,
                                           default=Decimal('0.00'),
                                           validators=[MinValueValidator(Decimal('0.00'))])
    custo_hospedagem = models.DecimalField("hospedagem",
                                           max_digits=5,
                                           decimal_places=2,
                                           default=Decimal('0.00'),
                                           validators=[MinValueValidator(Decimal('0.00'))])
    custo_outros = models.DecimalField("outros custos",
                                       max_digits=5,
                                       decimal_places=2,
                                       default=Decimal('0.00'),
                                       validators=[MinValueValidator(Decimal('0.00'))])
    pub_date = models.DateTimeField("data de publicacao", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('data_da_viagem', 'pub_date')
        verbose_name_plural = 'viagens'


class NotaFiscal(models.Model):
    loja = models.ForeignKey(Loja)
    numero = models.PositiveSmallIntegerField("número")
    data_da_nota = models.DateField(default=agora)
    viagem = models.ForeignKey(Viagem)
    pub_date = models.DateTimeField("data de cadastro", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('data_da_nota', 'pub_date')
        verbose_name_plural = 'Notas Fiscais'


class Venda(models.Model):
    numero_da_venda = models.PositiveSmallIntegerField("número da venda", unique=True)
    cliente = models.CharField(max_length=250, default="",
                               blank=True)
    data_da_venda = models.DateField(default=agora)
    FORMA_DE_PAGAMENTO_CHOICES = (
        ('DIN', 'dinheiro'),
        ('CAD', 'caderninho'),
        ('CAR', 'cartão'),
    )
    forma_de_pagamento = models.CharField(max_length=3,
                                          choices=FORMA_DE_PAGAMENTO_CHOICES,
                                          default='DIN')
    CADERNINHO_CHOICES = (
        ('DIN', 'dinheiro'),
        ('PAR', 'parcelado'),
        ('DEP', 'depósito'),
    )
    forma_caderninho = models.CharField(
                        "forma de pagamento no caderninho",
                        max_length=3,
                        choices=CADERNINHO_CHOICES,
                        default='PAR',
                        blank=True)
    CARTAO_CHOICES = (
        ('C', 'crédito'),
        ('D', 'débito'),
    )
    forma_cartao = models.CharField(
                    "forma de pagamento no cartão",
                    max_length=1,
                    choices=CARTAO_CHOICES,
                    default='C',
                    blank=True)
    PARCELA_CHOICES = (
        ('1', '1x'),
        ('2', '2x'),
        ('3', '3x'),
        ('4', '4x'),
    )
    numero_de_parcelas = models.CharField(max_length=1,
                                          choices=PARCELA_CHOICES,
                                          default='2', blank=True)

    pub_date = models.DateTimeField("data de cadastro", auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('data_da_venda', 'pub_date')
