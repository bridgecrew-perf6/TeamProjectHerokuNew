# Generated by Django 4.0.3 on 2022-03-24 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_dashboardmodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardmodel',
            name='table_id',
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
