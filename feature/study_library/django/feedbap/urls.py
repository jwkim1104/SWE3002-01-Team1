from django.conf.urls import url
from . import views
# url(r'^keyboard$', views.on_init),
urlpatterns = [
    url(r'^user_information_update$', views.user_information, name='user_information'),
    url(r'^index$', views.index_page, name='index_page'),
    url(r'^customize$', views.customize, name='customize'),
    url(r'^customize2$', views.customize2, name='customize2'),
    url(r'^customize3$', views.customize2, name='customize3'),
    url(r'^error$', views.error, name='error'),

]

# url(r'^customize_result$', views.customize2, name='customize_result'),
