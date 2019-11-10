from django.urls import path
from . import views



urlpatterns = [
    # home view /portfoliaTemplate/urls
    path('', views.home, name="home"),
    path('<int:projectName_id>/', views.result, name='Detail')
 
]