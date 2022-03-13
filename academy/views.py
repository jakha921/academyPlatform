from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Category, Course, Instructor, User, Source
from .forms import SignUpForm

# Create your views here.
class IndexListView(ListView):
    template_name = 'academy/index.html'
    model = Course
    context_object_name = 'courses'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()        
        return context
    
    def get_queryset(self, **kwargs):
        return Course.objects.filter(is_active = True)


def signup(request):
    return render(request, 'academy/signup.html')

class CourseDetailView(DetailView):
    model = Course
    template_name = "academy/course-detail.html"
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = Source.objects.all()        
        context['instructor'] = Instructor.objects.all()        
        return context
    

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = "academy/instructor-detail.html"
    pk_url_kwarg = 'pk'
    context_object_name = 'instructors'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


def grid_layout_with_sidebar(request):
    return render(request, 'academy/grid-layout-with-sidebar.html')

def find_instructor(request):
    return render(request, 'academy/find-instructor.html')

def about(request):
    return render(request, 'academy/about.html')

def dashboard(request):
    return render(request, 'academy/dashboard.html')

class SignUpCreateView(CreateView):
    model = User
    template_name = 'academy/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

def login(request):
    return render(request, 'academy/login.html')

def forgot(request):
    return render(request, 'academy/forgot.html')

def list_layout_with_sidebar(request):
    return render(request, 'academy/list-layout-with-sidebar.html')