# Generated by Django 3.0.14 on 2022-03-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
