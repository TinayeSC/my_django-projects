# Generated by Django 4.1.5 on 2023-01-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='signature',
            field=models.CharField(default='"TSC |n \'Enough turbulent meaninglessness creates purpose\' - Cixin Liu', max_length=140),
        ),
    ]
