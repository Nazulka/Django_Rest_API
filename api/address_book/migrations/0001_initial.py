# Generated by Django 3.2.7 on 2021-09-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('town', models.CharField(blank=True, max_length=40)),
                ('postcode', models.CharField(max_length=20)),
                ('country', models.CharField(default='UK', max_length=100)),
            ],
        ),
    ]
