from django.conf.urls import url
from . import views
# url(r'^keyboard$', views.on_init),
urlpatterns = [
    url(r'^user_information_update$', views.user_information, name='user_information'),
    url(r'^index$', views.index_page, name='index_page'),
]

