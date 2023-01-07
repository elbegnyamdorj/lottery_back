# Generated by Django 3.2.9 on 2022-01-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('plate_number', models.CharField(max_length=11)),
                ('date', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=50)),
                ('lottery_number', models.CharField(max_length=50)),
            ],
        ),
    ]