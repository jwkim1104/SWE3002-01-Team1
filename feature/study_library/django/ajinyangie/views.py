from django.shortcuts import render
from .models import Dog_types

# Create your views here.
def dog_types(request):
    return render(request, 'ajinyangie/dog_types.html', {'dogs':Dog_types.objects.all()})