# Generated by Django 3.0.2 on 2020-02-16 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=25, unique=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/recipe')),
                ('seen', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('img', models.ImageField(blank=True, null=True, upload_to='photos/recipe')),
                ('created_at', models.DateField(null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_no', models.IntegerField(default=1)),
                ('step_name', models.TextField(default=1)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Incredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('qty', models.FloatField()),
                ('unit', models.CharField(max_length=25)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.Recipe')),
            ],
        ),
    ]
