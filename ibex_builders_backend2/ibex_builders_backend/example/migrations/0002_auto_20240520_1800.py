# Generated by Django 3.2.12 on 2024-05-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='color',
            field=models.CharField(default='#2c3e50', max_length=20),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]