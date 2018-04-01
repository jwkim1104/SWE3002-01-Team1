from django.shortcuts import render
from .models import dog_types

# Create your views here.
def dog_types(request):
    return render(request, 'ajinyangie/dog_types.html', {'dog_types':dog_types})