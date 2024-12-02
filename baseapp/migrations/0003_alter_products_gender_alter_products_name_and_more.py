# Generated by Django 5.0.6 on 2024-10-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_remove_products_product_dis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('non_binary', 'Non-Binary'), ('Unisex', 'unisex')], default='gay', max_length=50, verbose_name='Gender specific'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=250, verbose_name='product name'),
        ),
        migrations.AlterField(
            model_name='products',
            name='wearat',
            field=models.CharField(blank=True, choices=[('casual', 'Casual'), ('formal', 'Formal'), ('party', 'Party'), ('weeding', 'Weeding'), ('sports', 'Sports')], max_length=150, verbose_name='Wear at'),
        ),
    ]
