# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_auto_20150225_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cidade',
            name='pais',
        ),
        migrations.AlterField(
            model_name='cidade',
            name='estado',
            field=models.CharField(default='PR', max_length=2, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notafiscal',
            name='data_da_nota',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 12, 23, 31, 610819, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venda',
            name='data_da_venda',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 12, 23, 31, 610819, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='viagem',
            name='data_da_viagem',
            field=models.DateField(default=datetime.datetime(2015, 2, 26, 12, 23, 31, 610819, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
