# Generated by Django 4.0.10 on 2023-06-20 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_delete_locker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=10)),
                ('unlock_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.unlocktime')),
            ],
        ),
    ]