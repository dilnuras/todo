# Generated by Django 3.1.3 on 2021-01-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210125_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]