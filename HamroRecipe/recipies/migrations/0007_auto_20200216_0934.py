# Generated by Django 3.0.2 on 2020-02-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0006_auto_20200216_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='r_name',
            field=models.CharField(max_length=25),
        ),
    ]