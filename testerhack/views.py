from django.shortcuts import render, redirect
from .models import UsersRedirect

# Create your views here.

percentage = 50
siteOne = 'page1.html'
siteTwo = 'page2.html'

def update_users():
    allUsers = UsersRedirect.objects.all()
    no_of_users = allUsers.count()
    base_line = int(no_of_users*percentage/100)
    new_site_users = allUsers[:base_line]
    for a in new_site_users:
        new_site_users.site(1)


def home(request):

    current_user = request.user

    if not current_user.is_authenticated():
        return redirect('/dash')

    if UsersRedirect.objects.filter(username=request.user.username).count() == 1 :
        if UsersRedirect.objects.filter(username=request.user.username).site() == 1 :
            return render(request, siteOne)
        else:
            return render(request, siteTwo)

    if current_user.is_superuser:
        return redirect('/dash')


def dash(request):

    return render(request, 'dash.html', context={'name' : request.user.username})

def login(request):
    
