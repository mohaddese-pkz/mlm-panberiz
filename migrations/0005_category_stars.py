# Generated by Django 4.0.5 on 2022-06-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlm', '0004_sellingpursant'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='stars',
            field=models.IntegerField(blank=True, null=True, verbose_name='stars'),
        ),
    ]
