from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^keyboard$', views.on_init),
    url(r'^message$', views.answer),
]

