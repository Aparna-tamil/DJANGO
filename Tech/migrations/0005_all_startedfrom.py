# Generated by Django 3.0.5 on 2020-04-15 11:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Tech', '0004_remove_all_startedfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='all',
            name='startedfrom',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 11, 47, 8, 721670, tzinfo=utc), verbose_name='started from'),
            preserve_default=False,
        ),
    ]
