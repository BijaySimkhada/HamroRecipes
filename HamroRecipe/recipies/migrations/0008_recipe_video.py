# Generated by Django 3.0.2 on 2020-02-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0007_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='video',
            field=models.FileField(blank=True, upload_to='videos/'),
        ),
    ]