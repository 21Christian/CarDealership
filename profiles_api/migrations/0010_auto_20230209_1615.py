# Generated by Django 2.2 on 2023-02-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0009_auto_20230209_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='number_of_tires',
            field=models.CharField(choices=[('2', 2), ('3', 3), ('4', 4)], default='', max_length=1),
        ),
    ]
