from django.urls import path
from . import views
app_name='movierecapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('details', views.details, name='Movie_details'),
]
