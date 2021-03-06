# Generated by Django 4.0 on 2022-03-11 22:11

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_instructor_email_instructor_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 3, 11, 19, 119171)),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='tutor_rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='active_courses',
            field=models.ManyToManyField(blank=True, help_text='optional. select courses you want to learn.', null=True, to='academy.Course'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Required. Inform a valid email address.', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, help_text='optional. 10 digits only.', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 3, 11, 19, 121171)),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
