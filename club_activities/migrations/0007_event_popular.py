# Generated by Django 2.1.1 on 2018-10-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_activities', '0006_auto_20181023_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='popular',
            field=models.IntegerField(choices=[('1', 'Add_In_front'), ('0', 'Dont_add')], default=0),
        ),
    ]
