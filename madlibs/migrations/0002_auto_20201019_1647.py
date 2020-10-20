# Generated by Django 2.2 on 2020-10-19 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madlibs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='madlibs',
            name='noun3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='madlibs',
            name='pronoun',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='madlibs',
            name='verb',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='madlibs',
            name='adjective',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='madlibs',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='madlibs',
            name='noun',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='madlibs',
            name='noun2',
            field=models.CharField(default='', max_length=20),
        ),
    ]