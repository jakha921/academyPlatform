from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('signup/', views.SignUpCreateView.as_view(), name='signup'),
    path('course-detail/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('instructor-detail/<int:pk>', views.InstructorListView.as_view(), name='instructor-detail'),
    path('about/', views.about, name='about'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('list-layout-with-sidebar/', views.ListLayoutWithSidebarListView.as_view(), name='list-layout-with-sidebar'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# handler_404 =

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