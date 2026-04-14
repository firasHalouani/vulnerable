from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("App running")

urlpatterns = [
    path('', home),
]