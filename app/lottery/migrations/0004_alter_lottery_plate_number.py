# Generated by Django 3.2.9 on 2022-01-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_alter_lottery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='plate_number',
            field=models.CharField(max_length=20),
        ),
    ]
