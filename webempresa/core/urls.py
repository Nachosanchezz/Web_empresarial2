from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name="index"),
    path('store.html', RedirectView.as_view(url='store/')),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('sample/', views.sample, name="sample"),
    
]