from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dogs$', views.dog_types, name='dog_types'),
    url(r'^keyboard', views.keyboard),
    url(r'^message$', views.answer),
]
