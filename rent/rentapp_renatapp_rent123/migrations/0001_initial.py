# Generated by Django 5.0.6 on 2024-06-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailRenter', models.CharField(max_length=50, unique=True)),
                ('nameRenter', models.CharField(max_length=50)),
                ('passwordRenter', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailSeller', models.CharField(max_length=50, unique=True)),
                ('nameSeller', models.CharField(max_length=50)),
                ('passwordSeller', models.CharField(max_length=15)),
            ],
        ),
    ]