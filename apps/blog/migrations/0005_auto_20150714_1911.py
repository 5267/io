# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150714_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=django_markdown.models.MarkdownField(null=True),
            preserve_default=True,
        ),
    ]
