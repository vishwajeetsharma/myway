# Generated by Django 3.1.4 on 2022-01-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20220119_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availablity',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='thi.ppng', upload_to='product_images/'),
            preserve_default=False,
        ),
    ]