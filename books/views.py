from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='home.html')

def about_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About Page")

