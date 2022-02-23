# Generated by Django 4.0.2 on 2022-02-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weatherModel',
            fields=[
                ('city', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('temprature', models.DecimalField(decimal_places=5, max_digits=5)),
                ('queryDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]