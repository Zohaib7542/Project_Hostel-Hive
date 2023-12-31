# Generated by Django 4.2.2 on 2023-06-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HostelHive', '0004_remove_booknow_adults'),
    ]

    operations = [
        migrations.AddField(
            model_name='booknow',
            name='adults',
            field=models.CharField(default=1, max_length=3),
        ),
        migrations.AlterField(
            model_name='booknow',
            name='children',
            field=models.CharField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='booknow',
            name='email',
            field=models.EmailField(max_length=3),
        ),
    ]
