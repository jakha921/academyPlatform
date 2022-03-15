# Generated by Django 4.0 on 2022-03-15 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_alter_category_icon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='course',
            new_name='themes',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 17, 21, 20, 38608)),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 15, 17, 21, 20, 41610)),
        ),
    ]
