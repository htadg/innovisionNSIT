from django.shortcuts import render, redirect
from .models import UsersRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

percentage = 50
siteOne = 'page1.html'
siteTwo = 'page2.html'


def populatemy():
    startUser = "user"
    startPass = "pass"
    for c in range(1, 51):
        user1 = UsersRedirect.objects.create(username=startUser+str(c),  password=(startPass+str(c)))
        user1.save()
        print "User Created"


def populatedjango():
    startUser = "user"
    startPass = "pass"
    for c in range(1, 51):
        user2 = User.objects.create_user(username=startUser+str(c), password=(startPass+str(c)))
        user2.save()
        print "Django User Created"


def update_users():
    allUsers = UsersRedirect.objects.all()
    no_of_users = allUsers.count()
    base_line = int(no_of_users*percentage/100)
    print base_line
    new_site_users = allUsers[:base_line]
    for a in new_site_users:
        a.site = 1
        a.save()
        print a.site
    print "IDs updated"


def home(request):
    if not UsersRedirect.objects.all().count() >= 45:
        populatemy()
    if not User.objects.all().count() >= 45:
        populatedjango()

    update_users()

    current_user = request.user

    if not current_user.is_authenticated():
        return redirect('/dash')

    if UsersRedirect.objects.filter(username=request.user.username).count() > 0 :
        if UsersRedirect.objects.filter(username=request.user.username)[0].site == 1 :
            return render(request, siteOne)
        else:
            return render(request, siteTwo)

    if current_user.is_superuser:
        return redirect('/dash')


def dash(request):

    return render(request, 'dash.html', context={'name' : request.user.username})


def login_user(request):
    if not UsersRedirect.objects.filter(username="user").count() > 0:
        UsersRedirect.objects.create(username="user", password="pass")
        UsersRedirect.objects.create(username="admin", password="admin")
    if request.method == "GET":
        context = {}
        if request.user.is_authenticated():
            context = {
                'authenticated' : True
            }
        return render(request, 'login.html', context)
    elif request.method == "POST":
        print "Post method Found"
        print UsersRedirect.objects.filter(username=request.POST['username'])
        if UsersRedirect.objects.filter(username=request.POST['username']).count() > 0 :
            print "user found"
            if UsersRedirect.objects.filter(username=request.POST['username']) and UsersRedirect.objects.filter(password=request.POST['password']) :
                print "user matched"
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return redirect('/')
            else:
                context = {
                    'valid': True
                }
                return render(request, 'login.html', context)
    return render(request, 'login.html', {'authenticated': False})


def logout_user(request):
    logout(request)
    return redirect('/login/')
