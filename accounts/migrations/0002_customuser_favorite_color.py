# Generated by Django 4.2 on 2023-08-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorite_color',
            field=models.TextField(null=True),
        ),
    ]