# Generated by Django 3.0.5 on 2020-04-15 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tech', '0003_auto_20200415_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all',
            name='startedfrom',
        ),
    ]