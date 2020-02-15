# Generated by Django 3.0.2 on 2020-02-14 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0006_auto_20200214_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step1', models.CharField(max_length=255)),
                ('step2', models.CharField(max_length=255)),
                ('step3', models.CharField(max_length=255)),
                ('step4', models.CharField(max_length=255)),
                ('step5', models.CharField(max_length=255)),
                ('step6', models.CharField(blank=True, max_length=255)),
                ('step7', models.CharField(blank=True, max_length=255)),
                ('step8', models.CharField(blank=True, max_length=255)),
                ('step9', models.CharField(blank=True, max_length=255)),
                ('step10', models.CharField(blank=True, max_length=255)),
                ('step11', models.CharField(blank=True, max_length=255)),
                ('r_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='recipies.Recipe')),
            ],
        ),
    ]
