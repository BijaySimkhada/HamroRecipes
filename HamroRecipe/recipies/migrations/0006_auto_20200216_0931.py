# Generated by Django 3.0.2 on 2020-02-16 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='r_name',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]