# Generated by Django 4.0.10 on 2023-06-17 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
