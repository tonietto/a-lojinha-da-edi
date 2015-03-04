from django.db import models
from django.utils import timezone
from django.db.models import permalink


agora = timezone.now()


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __unicode__(self):
        return '%s' % self.nome

    def __str__(self):
        return self.nome

    @permalink
    def get_absolute_url(self):
        return ('view_blog_categoria', None, {'slug': self.slug})

    class Meta:
        ordering = ('data_de_edicao',)


class Post(models.Model):
    titulo = models.CharField("título", max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    imagem = models.ImageField(upload_to='imagem_do_post')
    texto = models.TextField()
    categoria = models.ManyToManyField(Categoria)
    edicao = models.DateTimeField("editado em", default=agora)
    data_de_cadastro = models.DateTimeField("cadastro", auto_now_add=True)
    data_de_edicao = models.DateTimeField("edição", auto_now=True)

    def __unicode__(self):
        return '%s' % self.titulo

    def __str__(self):
        return self.titulo

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})

    class Meta:
        ordering = ('data_de_edicao',)
