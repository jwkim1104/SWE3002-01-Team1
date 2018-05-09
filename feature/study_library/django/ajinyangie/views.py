from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Dog_types
from django.http import JsonResponse
import json

# Create your views here.


def dog_types(request):
    return render(request, 'ajinyangie/dog_types.html', {'dogs':Dog_types.objects.all()})

# This is test version of chatbot System
# 2018.05.10 made by Kisung
# You should Check more information in ./urls.py


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘', '내일']
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '오늘':
        today = "오늘 급식"

        return JsonResponse({
            'message': {
                'text': today
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }

        })

    elif datacontent == '내일':
        tomorrow = "내일 급식"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }

        })
