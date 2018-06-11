from django.shortcuts import render
from .models import *
from ajinyangie.models import *
from django.http import JsonResponse
from .forms import PostForm
from django.shortcuts import redirect
import json
from feedbap.doginfocsv import *
from feedbap.final import *

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
    data = Dog_types.objects.all()
    data_dict = {}
    if request.method == "POST":
        sample_data = request.body
        sample_data = sample_data.decode('euc-kr').split('&')
        print(sample_data, "customize")
        data_dict["pet_id"] = int(sample_data[1].split('=')[1])
        data_dict["age"] = float(sample_data[2].split('=')[1])
        data_dict["breed_id"] = sample_data[3].split('=')[1].replace("+", " ")
        return render(request, 'feedbap/customize2.html', {
            'pet_id': str(data_dict["pet_id"]), 'age': str(data_dict["age"]),
            'breed_id': str(data_dict["breed_id"])})

    return render(request, 'feedbap/customize.html', {'breeds': data})


def customize2(request):
    if request.method == "POST":
        data_dict = {}
        sample_data = request.body
        sample_data = sample_data.decode('euc-kr').split('&')
        print(sample_data, "customize2 if>>>")

        if len(sample_data) < 5:
            data_dict["pet_id"] = int(sample_data[1].split('=')[1])
            data_dict["age"] = float(sample_data[2].split('=')[1])
            data_dict["breed_id"] = sample_data[3].split('=')[1].replace("+", " ")
            return render(request, 'feedbap/customize2.html', {
                'pet_id': str(data_dict["pet_id"]), 'age': str(data_dict["age"]),
                'breed_id': str(data_dict["breed_id"])})

        data_dict["pet_id"] = int(sample_data[1].split('=')[1])
        data_dict["age"] = float(sample_data[2].split('=')[1])
        data_dict["breed_id"] = sample_data[3].split('=')[1].replace("+", " ")
        data_dict["weight"] = float(sample_data[4].split('=')[1])
        data_dict["gender"] = int(sample_data[5].split('=')[1])
        data_dict["neut"] = int(sample_data[6].split('=')[1])
        data_dict["neut_date"] = sample_data[7].split('=')[1]
        return render(request, 'feedbap/customize2_2.html', {
            'pet_id': str(data_dict["pet_id"]), 'age': str(data_dict["age"]),
            'breed_id': str(data_dict["breed_id"]), 'weight': str(data_dict["weight"]),
            'gender': str(data_dict["gender"]), 'neut': str(data_dict["neut"]),
            'neut_data': str(data_dict["neut_date"])})


def customize2_2(request):
    if request.method == "POST":
        sample_data = request.body
        sample_data = sample_data.decode('euc-kr').split('&')
        print(sample_data, "customize2_2 if>>>")

        data_dict = {}
        if len(sample_data) < 9:
            data_dict["pet_id"] = int(sample_data[1].split('=')[1])
            data_dict["age"] = float(sample_data[2].split('=')[1])
            data_dict["breed_id"] = sample_data[3].split('=')[1].replace("+", " ")
            data_dict["weight"] = float(sample_data[4].split('=')[1])
            data_dict["gender"] = int(sample_data[5].split('=')[1])
            data_dict["neut"] = int(sample_data[6].split('=')[1])
            data_dict["neut_date"] = sample_data[7].split('=')[1]
            return render(request, 'feedbap/customize2_2.html', {
                'pet_id': str(data_dict["pet_id"]), 'age': str(data_dict["age"]),
                'breed_id': str(data_dict["breed_id"]), 'weight': str(data_dict["weight"]),
                'gender': str(data_dict["gender"]), 'neut': str(data_dict["neut"]),
                'neut_data': str(data_dict["neut_date"])})

        if len(sample_data) > 9:
            print(sample_data, "customize2_2 if>>>")
            data_dict["pet_id"] = int(sample_data[1].split('=')[1])
            data_dict["age"] = float(sample_data[2].split('=')[1])
            data_dict["breed_id"] = sample_data[3].split('=')[1].replace("+", " ")
            data_dict["weight"] = float(sample_data[4].split('=')[1])
            data_dict["gender"] = int(sample_data[5].split('=')[1])
            data_dict["neut"] = int(sample_data[6].split('=')[1])
            data_dict["neut_date"] = sample_data[7].split('=')[1]
            data_dict["obesity"] = int(sample_data[8].split('=')[1])
            data_dict["activity"] = int(sample_data[9].split('=')[1])
            data_dict["hi"] = sample_data[10].split('=')[1]
            data_dict["taste"] = sample_data[11].split('=')[1]
            return render(request, 'feedbap/customize3.html', {
                'pet_id': str(data_dict["pet_id"]), 'age': str(data_dict["age"]),
                'breed_id': str(data_dict["breed_id"]), 'weight': str(data_dict["weight"]),
                'gender': str(data_dict["gender"]), 'neut': str(data_dict["neut"]),
                'neut_data': str(data_dict["neut_date"]), 'obesity': str(data_dict["obesity"]),
                'activity': str(data_dict["activity"]), 'hi': str(data_dict['hi']), "taste": str(data_dict["taste"])})


def customize3(request):
    if request.method == "POST":
        sample_data = request.body
        sample_data = sample_data.decode('euc-kr').split('&')
        data_dict = {}
        data = Dog_types.objects.all()
        data_dict["pet_id"] = int(sample_data[1].split('=')[1])
        data_dict["age"] = float(sample_data[2].split('=')[1])
        data_dict["breed_id"] = sample_data[3].split('=')[1].replace("+", " ")
        data_dict["weight"] = float(sample_data[4].split('=')[1])
        data_dict["gender"] = int(sample_data[5].split('=')[1])
        data_dict["neut"] = int(sample_data[6].split('=')[1])
        data_dict["neut_date"] = sample_data[7].split('=')[1]
        data_dict["obesity"] = int(sample_data[8].split('=')[1])
        data_dict["activity"] = int(sample_data[9].split('=')[1])
        data_dict["hi"] = sample_data[10].split('=')[1]
        data_dict["taste"] = sample_data[11].split('=')[1]

        dog_info = []
        for index, item in enumerate(data):
            if item.weight is not None and item.life_span is not None:
                dog_info.append([index + 1, item.name, getWeightTuple(item.weight), getLifeTuple(item.life_span)])

        data_dict["pet_id"] = int(sample_data[1].split('=')[1])
        data_dict["age"] = float(sample_data[2].split('=')[1])
        data_dict["breed_id"] = sample_data[3].split('=')[1].replace("+", " ")
        data_dict["weight"] = float(sample_data[4].split('=')[1])
        data_dict["gender"] = int(sample_data[5].split('=')[1])
        data_dict["neut"] = int(sample_data[6].split('=')[1])
        data_dict["neut_date"] = sample_data[7].split('=')[1]
        data_dict["obesity"] = int(sample_data[8].split('=')[1])
        data_dict["activity"] = int(sample_data[9].split('=')[1])
        data_dict["hi"] = sample_data[10].split('=')[1]
        data_dict["taste"] = sample_data[11].split('=')[1]
        d = [
            data_dict["pet_id"],
            data_dict["age"],
            data_dict["breed_id"],
            data_dict["weight"],
            data_dict["gender"],
            data_dict["neut"],
            data_dict["neut_date"],
            data_dict["obesity"],
            data_dict["activity"],
            data_dict["hi"],
            data_dict["taste"]]

        result_dict = do_customize_main(dog_info, d)
        pet_id = result_dict["petID"]
        neut = result_dict["Neutralization"]
        age = result_dict["Age"]
        specifi = result_dict["Specification"]
        activity = result_dict["Activity"]
        activity_cal = result_dict["Activity Calculation"]
        obe = result_dict["Obesity"]
        size = result_dict["Size"]
        ingredient_set_number = result_dict["Ingredient Set Number"]
        is_weight_error = result_dict["error_weight"]
        print(is_weight_error, "testetsetestset")
        return render(request, 'feedbap/customize3.html', {
            'pet_id': pet_id, 'neut': neut, 'age': age,
            'specifi': specifi, 'activity': activity, 'activity_cal': activity_cal,
            'obe': obe, 'size': size, 'ingredient_set_number': ingredient_set_number,
            'is_weight_error': is_weight_error})
    return render(request, 'feedbap/customize3.html')


def error(request):
    return render(request, 'feedbap/error.html')