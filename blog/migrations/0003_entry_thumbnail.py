# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140704_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'thumbs/', blank=True),
        ),
    ]
