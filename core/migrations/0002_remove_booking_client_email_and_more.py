# Generated by Django 4.2.7 on 2025-06-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='client_email',
        ),
        migrations.RemoveField(
            model_name='fitnessclass',
            name='total_slots',
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(default=9999999999, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fitnessclass',
            name='available_slots',
            field=models.PositiveIntegerField(),
        ),
    ]
