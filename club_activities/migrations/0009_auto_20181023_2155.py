# Generated by Django 2.1.1 on 2018-10-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_activities', '0008_auto_20181023_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='mail',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='club',
            name='phone',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
    ]
