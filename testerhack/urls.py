from django.conf.urls import include, url

urlpatterns = [
    url(r'^dash$', 'testerhack.views.dash', name='dash'),
    url(r'^$', 'testerhack.views.home', name='home'),
]
