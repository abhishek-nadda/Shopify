# Generated by Django 3.0.5 on 2020-05-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200517_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mobile',
            field=models.IntegerField(default=9888811111),
            preserve_default=False,
        ),
    ]
