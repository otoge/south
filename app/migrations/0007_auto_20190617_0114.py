# Generated by Django 2.2 on 2019-06-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='scripts',
            field=models.ManyToManyField(blank=True, to='app.Item'),
        ),
    ]
