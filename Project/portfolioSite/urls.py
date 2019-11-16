from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('detail/', views.detail, name='detailView'),
    # detail view
    path('contact/', views.contact, name='contact'),
]




