from django.urls import path

from .views import home_view, about_view


urlpatterns = [
    path('', home_view, name='home_page'),
    path('about/', about_view, name='about_page'),
]
