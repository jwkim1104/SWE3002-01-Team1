from django.shortcuts import render
from .models import Dog_types


# Create your views here.


def dog_types(request):
    return render(request, 'ajinyangie/dog_types.html', {'dogs':Dog_types.objects.all()})

# This is test version of chatbot System
# 2018.05.10 made by Kisung
# You should Check more information in ./urls.py
