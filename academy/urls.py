from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('signup', views.SignUpCreateView.as_view(), name='signup'),
    path('course-detail/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('instructor-detail/<int:pk>', views.InstructorDetailView.as_view(), name='instructor-detail'),
    path('grid-layout-with-sidebar', views.grid_layout_with_sidebar, name='grid-layout-with-sidebar'),
    path('find-instructor', views.find_instructor, name='find-instructor'),
    path('about', views.about, name='about'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('forgot', views.forgot, name='forgot'),
    path('list-layout-with-sidebar', views.list_layout_with_sidebar, name='list-layout-with-sidebar'),
]

# template
"""urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    
    # path('detail/<int:question_id>/', views.detail, name='detail'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]"""