# Generated by Django 4.0.2 on 2022-03-02 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='order_status',
        ),
    ]
