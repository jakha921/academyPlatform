from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm 
from django.core.exceptions import ValidationError

from .models import Category, Course, Instructor, User, Source, Theme
from .forms import SignUpForm

# Create your views here.
class IndexListView(ListView):
    """return catergory & course models info"""
    template_name = 'academy/index.html'
    model = Course
    context_object_name = 'courses'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()        
        return context
    
    def get_queryset(self, **kwargs):
        return Course.objects.filter(is_active = True)


class CourseDetailView(DetailView):
    """"return course, source & instructor models info"""
    model = Course
    template_name = "academy/course-detail-4.html"
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        pk = kwargs['object'].id
        print(Theme.objects.filter(courses=pk))
        context = super().get_context_data(**kwargs)
        context['sources'] = Source.objects.all()      
        context['themes'] = Theme.objects.filter(courses=pk)       
        # context['themes'] = Theme.objects.all()       
        context['instructor'] = Instructor.objects.all()
        
        print(kwargs)  
        return context


class InstructorListView(ListView):
    """return instructor & course models info"""
    model = Instructor
    template_name = "academy/instructor-detail.html"
    pk_url_kwarg = 'pk'
    context_object_name = 'instructors'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class ListLayoutWithSidebarListView(ListView):
    model = Course
    template_name = 'academy/list-layout-with-sidebar.html'
    context_object_name = 'courses'
    pk_url_kwarg = 'pk'
    
    def get_queryset(self, **kwargs):
        return Course.objects.filter(is_active = True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = Source.objects.all()
        return context


class SignUpCreateView(CreateView):
    """create form for registration user"""
    model = User
    template_name = 'academy/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == '':
            raise ValidationError('Email is required')


class LoginUserView(LoginView):
    # template_name = 'academy/login.html'
    template_name = 'academy/test.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        return reverse_lazy('index')
    

def about(request):
    return render(request, 'academy/about.html')

def forgot(request):
    return render(request, 'academy/forgot.html')

def about(request):
    return render(request, 'academy/about.html')

def contact(request):
    return render(request, 'academy/contact.html')
