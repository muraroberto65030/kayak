# Generated by Django 3.1 on 2020-08-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0003_auto_20200818_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='configurazione',
            name='accettaautomaticamenteprenotazioni',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prenotazioni',
            name='accettata',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clienti',
            name='email',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]
