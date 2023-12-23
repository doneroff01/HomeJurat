from django.shortcuts import render
from django.views.generic import ListView
from .models import Home
# Create your views here.




class IndexView(ListView):
    model = Home
    template_name = 'index.html'