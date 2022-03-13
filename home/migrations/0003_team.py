# Generated by Django 3.0.14 on 2022-03-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220228_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('code', models.CharField(max_length=122)),
                ('points', models.IntegerField()),
                ('total_members', models.IntegerField(default=0)),
                ('P1', models.CharField(blank=True, max_length=122)),
                ('P2', models.CharField(blank=True, max_length=122)),
                ('P3', models.CharField(blank=True, max_length=122)),
                ('P4', models.CharField(blank=True, max_length=122)),
            ],
        ),
    ]
