# Generated by Django 4.0.5 on 2022-06-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('description', models.CharField(max_length=50)),
                ('currrencycode', models.CharField(max_length=15)),
                ('conversionrate', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='country',
        ),
    ]
