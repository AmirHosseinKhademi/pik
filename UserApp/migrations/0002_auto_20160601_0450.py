# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizeduser',
            name='debit_card',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
