# Generated by Django 2.2.6 on 2019-10-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0002_auto_20191011_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.ManyToManyField(to='bootcamp.Country'),
        ),
        migrations.AddField(
            model_name='client',
            name='language',
            field=models.ManyToManyField(to='bootcamp.Language'),
        ),
        migrations.AddField(
            model_name='client',
            name='payment',
            field=models.ManyToManyField(to='bootcamp.Payment'),
        ),
    ]
