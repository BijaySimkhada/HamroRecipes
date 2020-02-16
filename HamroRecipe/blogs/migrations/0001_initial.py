# Generated by Django 3.0.2 on 2020-02-16 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=25)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='photos/blog/')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
