from webbrowser import get
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe

from datetime import datetime


# Create your models here.
class Instructor(models.Model):
    """teacher information"""
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    avatar = models.ImageField(upload_to='avatars/')
    short_description = models.TextField()
    tutor_rating = models.FloatField(default=0, validators=[
        MinValueValidator(0.0), MaxValueValidator(5.0)])
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linked_in = models.URLField(blank=True)
    git_hub = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    registration_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Category(models.Model):
    """field of activity in with sphere of education (frontend, backend, fullstack, etc.)"""
    title = models.CharField(max_length=200)
    icon = models.CharField(
        max_length=25, help_text='https://www.w3schools.com/icons/fontawesome5_icons_alert.asp  https://fontawesome.ru/cheatsheet/\n\tExapmle: fa fa-code')
    number_of_courses = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def get_image_preview(self):
        if self.icon:
            return mark_safe('<i class="%s"></i>' % self.icon)
        else:
            return 'Image not found'

    def get_count_of_courses_in_category(self):
        return Course.objects.filter(categories=self).count()

    get_image_preview.short_description = 'image'
    get_count_of_courses_in_category.short_description = 'Number of courses'

    number_of_courses = get_count_of_courses_in_category

    def __str__(self):
        return self.title


class Course(models.Model):
    """which part or language will be study in this course"""
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.FloatField(default=0, validators=[
        MinValueValidator(0.0), MaxValueValidator(5.0)], editable=False)
    overview = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True, choices=[(
        'Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    course_include = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0)
    preview_image = models.ImageField(
        upload_to='course_image/', blank=True, null=True, help_text='Image size should be at least 1200x800')
    author = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Theme(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    theme_name = models.CharField(max_length=255)

    def __str__(self):
        return self.theme_name


class Source(models.Model):
    themes = models.ForeignKey(Theme, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    video = models.URLField(blank=True, null=True,
                            help_text='Youtube video link')
    video_duration = models.CharField(max_length=8, blank=True, null=True)
    pdf = models.URLField(blank=True, null=True, help_text='PDF file link')
    script = models.FileField(
        upload_to='script/', blank=True, null=True, help_text='upload script file')
    is_viewed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class User(models.Model):
    """create user model necessary data is username, firstname, lastname, email, password and other is optionally"""
    username = models.CharField(max_length=30, blank=True)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=254, unique=True)
    phone = models.IntegerField(
        blank=True, null=True)
    password = models.CharField(
        max_length=20)
    description = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    active_courses = models.ManyToManyField(
        Course, blank=True, null=True, help_text='optional. select courses you want to learn.')
    registration_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0, validators=[
        MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return str(self.user) + ' ' + str(self.course)


# class Feedback(models.Model):
#     name = models.CharField(max_length=150, editable=False, blank=True)
#     email = models.EmailField(max_length=255, editable=False)
#     feedback = models.TextField(editable=False)
#     date = models.DateTimeField(auto_now_add=True, editable=False)

#     def __str__(self):
#         return self.name
