from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from .forms import PostForm
from django.shortcuts import redirect
import json


# Create your views here.
def user_information(request):
    if request.method == "POST":
        sample_data = request.body
        sample_data = sample_data.decode('euc-kr').split('&')
        new_name = sample_data[1].split('=')[1]
        new_email = sample_data[2].split('=')[1]
        new_phone = sample_data[3].split('=')[1]

        test_object = User.objects.get(serialNum='0001')
        if new_name != '':
            test_object.userName = new_name
        if new_email != '':
            test_object.email = new_email
        if new_phone != '':
            test_object.phonenumber = new_phone
        test_object.save()
        return render(request, 'feedbap/user_information_update.html', {'users': User.objects.all()})

    return render(request, 'feedbap/user_information_update.html', {'users': User.objects.all()})


def index_page(request):
    return render(request, 'feedbap/index_page.html')
