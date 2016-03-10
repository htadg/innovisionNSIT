from django.conf.urls import include, url

urlpatterns = [
    url(r'^dash/$', 'testerhack.views.dash', name='dash'),
    url(r'^$', 'testerhack.views.home', name='home'),
    url(r'^login/$', 'testerhack.views.login_user', name='login'),
    url(r'^logout/$', 'testerhack.views.logout_user', name='logout'),
    url(r'^style/oldpage$','testerhack.views.pageOne', name='pageOne'),
    url(r'^style/newpage$','testerhack.views.pageTwo', name='pageTwo'),
    url(r'^statistics/$', 'testerhack.views.statistics', name='statistics'),
]
