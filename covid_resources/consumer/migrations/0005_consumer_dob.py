# Generated by Django 3.2.3 on 2021-05-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0004_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
