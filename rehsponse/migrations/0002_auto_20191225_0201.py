# Generated by Django 3.0.1 on 2019-12-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehsponse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]