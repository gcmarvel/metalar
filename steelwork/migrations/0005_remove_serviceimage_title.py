# Generated by Django 2.2.9 on 2020-06-03 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steelwork', '0004_auto_20200603_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceimage',
            name='title',
        ),
    ]
