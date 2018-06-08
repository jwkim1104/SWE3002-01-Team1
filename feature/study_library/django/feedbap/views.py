from django.shortcuts import render
from .models import *
from ajinyangie.models import *
from django.http import JsonResponse
from .forms import PostForm
from django.shortcuts import redirect
import json
from feedbap.doginfocsv import *


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


def customize(request):
    if request.method == "POST":
        data = Dog_types.objects.all()
        dog_info = []
        for index, item in enumerate(data):
            if item.weight is not None and item.life_span is not None:
                dog_info.append([index+1, item.name, getTuple(item.weight), getTuple(item.life_span)])
        sample_data = request.body
        sample_data = sample_data.decode('euc-kr').split('&')
        data1 = sample_data[1].split('=')[1]
        data2 = sample_data[2].split('=')[1].replace("+", " ")
        data3 = sample_data[3].split('=')[1]
        data4 = sample_data[4].split('=')[1]
        data5 = sample_data[5].split('=')[1]
        sample_list = [data1, data2, int(data3), int(data4), int(data5)]
        result_list = getAnalysis(dog_info, sample_list)
        return render(request, 'feedbap/customize_result.html', {
            'dog_name': data1, 'dog_id': result_list[0], 'obe': result_list[1], 'work_out': result_list[2]})
    return render(request, 'feedbap/customize.html')

