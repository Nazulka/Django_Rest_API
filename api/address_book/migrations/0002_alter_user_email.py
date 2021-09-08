# Generated by Django 3.2.7 on 2021-09-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Email already exists'}, max_length=50, unique=True),
        ),
    ]
