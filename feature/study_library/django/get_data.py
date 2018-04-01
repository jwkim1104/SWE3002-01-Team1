import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testsite.settings')

import django
django.setup()
from ajinyangie.models import dog_types

import requests
from bs4 import BeautifulSoup

def get_object(dog_name, sample_dict):
    dog_types.objects.create(
        name = dog_name,
        group = sample_dict["group"],
        height = sample_dict["height"],
        weight = sample_dict["weight"],
        life_span = sample_dict["life_span"]
    )
    return

API = 'http://dogtime.com/dog-breeds/'
get_dog_name = requests.get(API)
dog_name_soup = BeautifulSoup(get_dog_name.text, 'html.parser')
for dog_name in dog_name_soup.find_all("a", attrs={"class": "post-title"}):
    get_dog_data = requests.get(API + dog_name.string.replace(' ', '-') + '#/slide/1')
    get_dog_data_soup = BeautifulSoup(get_dog_data.text, 'html.parser')
    dog_name = dog_name.string
    sample_dict = {}
    for index, dog_data in enumerate(get_dog_data_soup.select("div[class=\"inside-box\"]")[1]):
        if index == 2:
            sample_dict["group"] = dog_data
        elif index == 5:
            sample_dict["height"] = dog_data
        elif index == 8:
            sample_dict["weight"] = dog_data
        elif index == 11:
            sample_dict["life_span"] = dog_data
        else :
            continue
    print(sample_dict)
    get_object(dog_name, sample_dict)
    break

