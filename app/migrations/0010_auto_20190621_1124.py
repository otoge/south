# Generated by Django 2.2 on 2019-06-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190621_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='scripts',
            field=models.ManyToManyField(blank=True, to='app.Item'),
        ),
    ]