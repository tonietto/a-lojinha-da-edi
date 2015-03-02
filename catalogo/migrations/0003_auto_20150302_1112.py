# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20150302_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peca',
            name='imagem_1',
            field=models.ImageField(blank=True, upload_to='uploads/imagens/pecas/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='peca',
            name='imagem_2',
            field=models.ImageField(blank=True, upload_to='uploads/imagens/pecas/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='peca',
            name='imagem_3',
            field=models.ImageField(blank=True, upload_to='uploads/imagens/pecas/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='peca',
            name='imagem_4',
            field=models.ImageField(blank=True, upload_to='uploads/imagens/pecas/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tamanhodapeca',
            name='tamanho',
            field=models.CharField(unique=True, max_length=3),
            preserve_default=True,
        ),
    ]
