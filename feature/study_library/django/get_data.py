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

def return_parsed(before_parsed):
    if before_parsed == "Dog Breed Group:":
        return "group"
    elif before_parsed == "Height:":
        return "height"
    elif before_parsed == "Weight:":
        return "weight"
    else :
        return "life_span"

API = 'http://dogtime.com/dog-breeds/'
get_dog_name = requests.get(API)
dog_name_soup = BeautifulSoup(get_dog_name.text, 'html.parser')
for dog_name in dog_name_soup.find_all("a", attrs={"class": "post-title"}):
    get_dog_data = requests.get(API + dog_name.string.replace(' ', '-') + '#/slide/1')
    get_dog_data_soup = BeautifulSoup(get_dog_data.text, 'html.parser')
    dog_name = dog_name.string
    dog_dict = {'group':None, 'height':None, 'weight':None, 'life_span':None}
    index_list = []
    try :
        dog_data_list = list(get_dog_data_soup.select("div[class=\"inside-box\"]")[1])
        for index, element_data in enumerate(dog_data_list):
            if str(type(element_data)) == "<class 'bs4.element.NavigableString'>":
                index_list.append(index)
        for data_index in index_list:
            dog_dict[return_parsed(dog_data_list[data_index-1].string)] = dog_data_list[data_index]
        print(dog_dict)
        get_object(dog_name, dog_dict)
    except IndexError:
        continue
