from django.conf.urls import url
from . import views
# url(r'^keyboard$', views.on_init),
urlpatterns = [
    url(r'^user_information_update$', views.user_information, name='user_information'),
    url(r'^index$', views.index_page, name='index_page'),
    url(r'^customize$', views.customize, name='customize'),
    url(r'^customize_result$', views.customize, name='customize_result'),

]

