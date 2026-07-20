from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_url, name='home_url'),
    path('shortlink/<int:id>/', views.show_url, name='show_url'),
    path('<str:short_code>/', views.redirect_to_original, name='redirect_to_original')
]
