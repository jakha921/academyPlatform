from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('course-detail', views.course_detail, name='course-detail'),
    path('instructor-detail', views.instructor_detail, name='instructor-detail'),
    path('grid-layout-with-sidebar', views.grid_layout_with_sidebar, name='grid-layout-with-sidebar'),
    path('find-instructor', views.find_instructor, name='find-instructor'),
    path('about', views.about, name='about'),
    path('dashboard', views.dashboard, name='dashboard'),
]
