# Generated by Django 3.1.3 on 2021-01-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210122_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.DateTimeField(),
        ),
    ]
