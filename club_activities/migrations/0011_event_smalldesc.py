# Generated by Django 2.1.1 on 2018-10-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_activities', '0010_auto_20181023_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='smalldesc',
            field=models.TextField(null=True),
        ),
    ]
