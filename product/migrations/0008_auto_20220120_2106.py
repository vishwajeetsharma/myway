# Generated by Django 3.1.4 on 2022-01-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20220120_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promo_codes',
            field=models.ManyToManyField(blank=True, to='product.Promo_code'),
        ),
    ]
