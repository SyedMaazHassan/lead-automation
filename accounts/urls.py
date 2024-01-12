from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('email-templates', views.all_templates, name='template-list'),
    path('create-template', views.create_template, name='create-template'),
    path('leads', views.all_leads, name='leads'),
    path('single-lead', views.single_leads, name='single-lead'),    
    path('with-with-ai', views.write_with_ai, name='write-with-ai'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
