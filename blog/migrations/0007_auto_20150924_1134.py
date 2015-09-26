# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150924_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='thumbnail',
            field=models.ImageField(upload_to='media/', null=True, blank=True),
        ),
    ]
