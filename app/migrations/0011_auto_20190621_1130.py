# Generated by Django 2.2 on 2019-06-21 02:30

from django.db import migrations ,models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190621_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='scripts',
            field=models.ManyToManyField(blank=True, to='app.Item'),
        ),

        migrations.AddField(
            model_name='profile',
            name='scripts',
            field=models.ManyToManyField(blank=True, through='app.Quote', to='app.Item'),
        ),
    ]
