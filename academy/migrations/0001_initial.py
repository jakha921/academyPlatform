# Generated by Django 4.0 on 2022-03-11 19:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to='icons/', verbose_name='')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rate', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('overview', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('level', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=100, null=True)),
                ('course_include', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0)),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='course_image/', verbose_name='')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, editable=False, max_length=150)),
                ('email', models.EmailField(editable=False, max_length=255)),
                ('feedback', models.TextField(editable=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('short_description', models.TextField()),
                ('tutor_rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('instagram', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('linked_in', models.URLField(blank=True)),
                ('git_hub', models.URLField(blank=True)),
                ('portfolio', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('active_courses', models.ManyToManyField(blank=True, null=True, to='academy.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.ManyToManyField(to='academy.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='academy.Category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.user')),
            ],
        ),
    ]