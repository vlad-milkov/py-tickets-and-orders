# Generated by Django 4.0.2 on 2022-10-08 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
    ]