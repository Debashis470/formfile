from django.urls import path
from .views import create_personal_info
urlpatterns = [
    path('personal-info/', create_personal_info, name='create_personal_info'),
]