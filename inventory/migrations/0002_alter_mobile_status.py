# Generated by Django 4.2.3 on 2024-11-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('new', '+'), ('used', '-')], max_length=50),
        ),
    ]
