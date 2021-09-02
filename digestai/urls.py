from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('summarize/', views.summarize, name='summarize'),
    path('summarize/new/', views.create_summary, name='create_summary'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('library/', views.library, name='library'),
    path('activity/', views.activity, name='activity'),
    path('account/', views.account, name='account'),
    path('studyset/', views.studyset, name='studyset'),
    path('info/', views.info, name='info'),

    path('api/studysets', views.studyset_list), # GET, POST, DELETE
    path('api/studysets/<pk>', views.studyset_details), # GET, PUT, DELETE
]

 
