from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'academy/index.html')

def signup(request):
    return render(request, 'academy/signup.html')

def course_detail(request):
    return render(request, 'academy/course-detail.html')

def instructor_detail(request):
    return render(request, 'academy/instructor-detail.html')

def grid_layout_with_sidebar(request):
    return render(request, 'academy/grid-layout-with-sidebar.html')

def find_instructor(request):
    return render(request, 'academy/find-instructor.html')

def about(request):
    return render(request, 'academy/about.html')

def dashboard(request):
    return render(request, 'academy/dashboard.html')