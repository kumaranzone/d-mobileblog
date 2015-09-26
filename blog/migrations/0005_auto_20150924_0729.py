# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150924_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=(b'/home/pythonuser/works/qblog/static',), blank=True),
        ),
    ]
