# Generated by Django 3.2.3 on 2021-05-30 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0008_merge_20210529_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
