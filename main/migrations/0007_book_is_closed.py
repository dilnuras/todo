# Generated by Django 3.1.3 on 2021-01-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_book_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]