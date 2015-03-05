from django.db import models
from django.core.validators import MinValueValidator
# from django.contrib.humanize.templatetags.humanize import naturalday
from django.utils import timezone
from django.utils.html import format_html

from decimal import Decimal


NOTA_CHOICES = (
    ('0', 'Péssimo'),
    ('1', 'Ruim'),
    ('2', 'Regular'),
    ('3', 'Bom'),
    ('4', 'Ótimo'),
    ('5', 'Excelente'),
)


agora = timezone.now()


class Cidade(models.Model):
    cidade = models.CharField(max_length=30)
    ESTADOS_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    estado = models.CharField(max_length=2,
                              choices=ESTADOS_CHOICES,
                              default='PR')
    anotacoes = models.TextField("anotações", blank=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.cidade

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "cidade__icontains",)

    class Meta:
        ordering = ('data_de_edicao',)


class Shopping(models.Model):
    nome = models.CharField(max_length=30)
    cidade = models.ForeignKey(Cidade)
    rua = models.CharField(max_length=150, blank=True)
    numero = models.PositiveSmallIntegerField("número", blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True)
    nota = models.CharField(max_length=1, choices=NOTA_CHOICES, default=3)
    anotacoes = models.TextField("anotações", blank=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "nome__icontains",)

    def endereco(self):
        return format_html(self.rua + ', ' + str(self.numero) + ', ' + str(self.complemento) + '. ' + self.bairro + ' - <strong>' + str(self.cidade) + '</strong>.')

    endereco.short_description = 'endereço'
    endereco.allow_tags = True

    class Meta:
        ordering = ('data_de_edicao',)


class Guia(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30, blank=True)
    cidade = models.ForeignKey(Cidade)
    email = models.EmailField(max_length=254, blank=True)
    telefone = models.PositiveSmallIntegerField(blank=True, null=True)
    shoppings = models.ManyToManyField(Shopping)
    nota = models.CharField(max_length=1, choices=NOTA_CHOICES, default=3)
    anotacoes = models.TextField("anotações", blank=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.nome

    def nome_completo(self):
        return format_html(self.nome + ' ' + self.sobrenome)

    def get_telefone(self):
        return "(%c%c)%c%c%c%c-%c%c%c%c" % tuple(map(ord, str(self.telefone)))

    get_telefone.short_description = 'telefone'

    def get_shoppings(self):
        return ", <br/>".join([p.nome for p in self.shoppings.all()[:5]])

    get_shoppings.short_description = 'shoppings'
    get_shoppings.allow_tags = True

    class Meta:
        ordering = ('data_de_edicao',)


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
    nota = models.CharField(max_length=1, choices=NOTA_CHOICES, default=3)
    anotacoes = models.TextField("anotações", blank=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.nome

    def get_telefone(self):
        return "(%c%c)%c%c%c%c-%c%c%c%c" % tuple(map(ord, str(self.telefone)))

    get_telefone.short_description = 'telefone'

    def get_cnpj(self):
        return "%c%c.%c%c%c.%c%c%c/%c%c%c%c-%c%c" % tuple(map(ord, str(self.cnpj)))

    get_cnpj.short_description = 'cnpj'

    class Meta:
        ordering = ('data_de_edicao',)


class Marca(models.Model):
    nome = models.CharField(max_length=30)
    nota = models.CharField(max_length=1, choices=NOTA_CHOICES, default=3)
    anotacoes = models.TextField("anotações", blank=True)
    imagem = models.ImageField(upload_to='uploads/imagens/marcas', blank=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.nome

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "nome__icontains",)

    class Meta:
        ordering = ('data_de_edicao',)


class Viagem(models.Model):
    data = models.DateField(default=agora)
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
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        nome = str(self.cidade) + ' ' + ' (' + (self.data).strftime('%d/%m/%Y') + ')'
        return nome

    def combustivel(self):
        return "R$%s" % self.custo_combustivel if self.custo_combustivel else ""

    combustivel.short_description = 'combustível'

    def pedagios(self):
        return "R$%s" % self.custo_pedagios if self.custo_pedagios else ""

    pedagios.short_description = 'pedágios'

    def alimentacao(self):
        return "R$%s" % self.custo_alimentacao if self.custo_alimentacao else ""

    alimentacao.short_description = 'alimentação'

    def estacionamento(self):
        return "R$%s" % self.custo_estacionamento if self.custo_estacionamento else ""

    def transporte(self):
        return "R$%s" % self.custo_transporte if self.custo_transporte else ""

    def hospedagem(self):
        return "R$%s" % self.custo_hospedagem if self.custo_hospedagem else ""

    def outros(self):
        return "R$%s" % self.custo_outros if self.custo_outros else ""

    @property
    def custo_total(self):
        calculo = self.custo_combustivel + self.custo_pedagios + self.custo_alimentacao + self.custo_estacionamento + self.custo_transporte + self.custo_hospedagem + self.custo_outros
        return "R$%s" % calculo if calculo else ""

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "nome__icontains",)

    class Meta:
        ordering = ('data_de_edicao',)
        verbose_name_plural = 'viagens'


class Recibo(models.Model):
    loja = models.ForeignKey(Loja)
    RECIBO_CHOICES = (
        ('1', 'Romaneio'),
        ('2', 'Nota Fiscal'),
    )
    tipo = models.CharField(max_length=1, choices=RECIBO_CHOICES, default=1)
    numero = models.PositiveSmallIntegerField("número", blank=True, null=True)
    viagem = models.ForeignKey(Viagem)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        nome = str(self.loja) + ' ' + ' (' + str(self.viagem) + ')'
        return nome

    class Meta:
        ordering = ('data_de_edicao',)


class Venda(models.Model):
    cliente = models.ForeignKey('cliente.Cliente', blank=True)
    data = models.DateField(default=agora)
    FORMA_DE_PAGAMENTO_CHOICES = (
        ('DIN', 'dinheiro'),
        ('CAD', 'caderninho'),
        ('CAR', 'cartão'),
        ('PGS', 'PagSeguro'),
    )
    forma_de_pagamento = models.CharField(max_length=3,
                                          choices=FORMA_DE_PAGAMENTO_CHOICES)
    CADERNINHO_CHOICES = (
        ('DIN', 'dinheiro'),
        ('PAR', 'parcelado'),
        ('DEP', 'depósito'),
    )
    forma_caderninho = models.CharField(
                        "forma de pagamento no caderninho",
                        max_length=3,
                        choices=CADERNINHO_CHOICES,
                        blank=True)
    CARTAO_CHOICES = (
        ('C', 'crédito'),
        ('D', 'débito'),
    )
    forma_cartao = models.CharField(
                    "forma de pagamento no cartão",
                    max_length=1,
                    choices=CARTAO_CHOICES,
                    blank=True)
    PARCELA_CHOICES = (
        ('1', '1x'),
        ('2', '2x'),
        ('3', '3x'),
        ('4', '4x'),
    )
    numero_de_parcelas = models.CharField(max_length=1,
                                          choices=PARCELA_CHOICES,
                                          blank=True)
    STATUS_VENDA_CHOICES = (
        ('0', 'aberta'),
        ('1', 'encerrada'),
    )
    status_venda = models.CharField(
                                    max_length=1,
                                    choices=STATUS_VENDA_CHOICES,
                                    default=0,
                                    blank=True, null=True
                                    )
    STATUS_PECA_CHOICES = (
        ('0', 'aguardando cliente'),
        ('1', 'em trânsito'),
        ('2', 'entregue'),
    )
    status_peca = models.CharField(
                                   "status peça",
                                   max_length=1,
                                   choices=STATUS_PECA_CHOICES,
                                   blank=True, null=True
                                   )
    data_de_cadastro = models.DateTimeField("abertura", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)
    data_de_fechamento = models.DateTimeField("fechamento",
                                              blank=True, null=True)  # To-do

    def __str__(self):
        return str(self.cliente) + ' ' + ' (' + str(self.data) + ')'

    class Meta:
        ordering = ('data_de_edicao',)


class Peca(models.Model):
    venda = models.ForeignKey(Venda)
    peca = models.ManyToManyField('catalogo.Peca', verbose_name='peça')
    tamanhos = models.ManyToManyField('catalogo.TamanhoDaPeca')
    quantidade = models.PositiveSmallIntegerField(default=1)
    valor_venda = models.DecimalField("valor venda", max_digits=5,
                                      decimal_places=2,
                                      blank=True, null=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __str__(self):
        return self.peca

    class Meta:
        ordering = ('data_de_edicao',)
        verbose_name = "peça"


class Parcela(models.Model):
    venda = models.ForeignKey(Venda)
    numero = models.PositiveSmallIntegerField("número da parcela", default=0)
    data = models.DateField(default=agora)
    valor = models.DecimalField(max_digits=5,
                                decimal_places=2,
                                default=Decimal('0.00'),
                                validators=[MinValueValidator(Decimal('0.00'))])
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    class Meta:
        ordering = ('data_de_edicao',)
