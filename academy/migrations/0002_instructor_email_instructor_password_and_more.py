# Generated by Django 4.0 on 2022-03-11 20:55

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.EmailField(default='admin@admin.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructor',
            name='password',
            field=models.CharField(default='12345678', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructor',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 1, 54, 54, 147213), editable=False),
        ),
        migrations.RemoveField(
            model_name='course',
            name='author',
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academy.instructor'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='course',
            name='categories',
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academy.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='rate',
            field=models.FloatField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='tutor_rating',
            field=models.FloatField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
