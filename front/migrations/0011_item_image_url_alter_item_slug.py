# Generated by Django 4.0.2 on 2022-03-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0010_payments_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
