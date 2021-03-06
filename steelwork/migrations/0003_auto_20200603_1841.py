# Generated by Django 2.2.9 on 2020-06-03 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steelwork', '0002_auto_20200126_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
        migrations.AddField(
            model_name='service',
            name='main_image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Титульное изображение'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Главное изображение')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='steelwork.Service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Изображение услуги',
                'verbose_name_plural': 'Изображения услуг',
            },
        ),
    ]
