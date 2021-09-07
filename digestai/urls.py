from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views
from . import auth

from django.views.decorators.csrf import csrf_exempt


schema_view = get_schema_view(
    openapi.Info(
        title="DigestAI API",
        default_version='v1',
        description="Backend API",
        terms_of_service="https://digestai.com/terms",
        contact=openapi.Contact(email="contact@digestai.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    #path('', views.index, name='index'),
    #path('summarize/', views.summarize, name='summarize'),
    #path('summarize/new/', views.create_summary, name='create_summary'),
    #path('login/', views.login, name='login'),
    #path('signup/', views.signup, name='signup'),
    #path('library/', views.library, name='library'),
    #path('activity/', views.activity, name='activity'),
    #path('account/', views.account, name='account'),
    #path('studyset/', views.studyset, name='studyset'),
    #path('info/', views.info, name='info'),
    path('test-signup/', csrf_exempt(auth.user_signup)),

    path('api/studysets', views.studyset_list), # GET, POST, DELETE
    path('api/studysets/<pk>', views.studyset_details), # GET, PUT, DELETE
    path('api/user', views.user_details), # GET, PUT, POST, DELETE

    ## Worker services
    path('api/summarize', views.summarize), # POST
    path('api/flashcards', views.generate_flashcards), # POST
    path('api/quiz/new', views.generate_quiz), # POST
    path('api/quiz/evaluate', views.evaluate_quiz), # POST

    # API Documentation
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

