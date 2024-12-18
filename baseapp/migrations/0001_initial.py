# Generated by Django 5.0.6 on 2024-10-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, verbose_name='product name')),
                ('product_type', models.CharField(max_length=50, verbose_name='product type')),
                ('product_dis', models.TextField(verbose_name='product description')),
                ('product_season', models.CharField(max_length=80, verbose_name='product wear season')),
                ('product_wearat', models.CharField(max_length=150, verbose_name='')),
                ('product_gender', models.CharField(max_length=50, verbose_name='')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'products',
                'verbose_name_plural': ' productss',
            },
        ),
    ]
