from django.shortcuts import render, redirect
from .models import UsersRedirect, SettingsUser, AnalyticsTwo, AnalyticsOne
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

percentage = 50
siteTwo = 'page1.html'
siteOne = 'page2.html'


if not SettingsUser.objects.all().count() > 0:
    setting = SettingsUser.objects.create(id=1, percentage = percentage)
    stat1 = AnalyticsOne.objects.create(id=1)
    stat2 = AnalyticsTwo.objects.create(id=1)
else:
    setting = SettingsUser.objects.filter(id=1)[0]
    stat1 = AnalyticsOne.objects.filter(id=1)[0]
    stat2 = AnalyticsTwo.objects.filter(id=1)[0]


def suggest():
    global purchase_ratio1
    global purchase_ratio2
    global suggestion
    purchase_ratio1 = float(stat1.buy) / float(stat1.visit)
    purchase_ratio2 = float(stat2.buy) / float(stat2.visit)
    suggestion = int(purchase_ratio2*100/(purchase_ratio2+purchase_ratio1))
    return  suggestion


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
    no_of_users = int(allUsers.count())
    base_line = int(no_of_users*int(percentage)/100)
    print base_line
    new_site_users = allUsers[:base_line]
    for a in new_site_users:
        a.site = 1
        a.save()
        print a.site
    print "IDs updated"


def home(request):

    global stat1
    global stat2

    if not UsersRedirect.objects.all().count() >= 45:
        populatemy()
    if not User.objects.all().count() >= 45:
        populatedjango()

    update_users()

    current_user = request.user

    if not current_user.is_authenticated():
        return redirect('/login')

    if request.method == "POST":
        if UsersRedirect.objects.filter(username=request.user.username)[0].site == 1:
            stat2.buy += 1
            stat2.save()
        else:
            stat1.buy += 1
            stat1.save()
        return render(request, 'thanks.html')

    if UsersRedirect.objects.filter(username=request.user.username).count() > 0 :
        if UsersRedirect.objects.filter(username=request.user.username)[0].site == 1 :
            stat2.visit += 1
            stat2.save()
            return render(request, siteOne)
        else:
            stat1.visit += 1
            stat1.save()
            return render(request, siteTwo)

    if current_user.is_superuser:
        return redirect('/dash')


def dash(request):
    if not request.user.is_superuser:
        return redirect('/')
    global setting
    context = {
        'value': setting.percentage,
        'suggestion': suggest()
    }
    if request.method == "GET":
        return render(request, 'dash.html', context)
    elif request.method == "POST":
        global percentage
        percentage = request.POST['percent']
        setting.percentage = percentage
        setting.save()
        update_users()
        return redirect('/dash/')


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
                print "user authenticated"
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


def pageOne(request):
    return render(request, siteOne)

def pageTwo(request):
    return render(request, siteTwo)

def statistics(request):

    global stat1
    global stat2

    if not request.user.is_superuser:
        return redirect('/')
    else:
        purchase_ratio1 = float(stat1.buy) / float(stat1.visit)
        purchase_ratio2 = float(stat2.buy) / float(stat2.visit)
        context={
            'stat1_visit': stat1.visit,
            'stat1_buy': stat1.buy,
            'stat2_visit': stat2.visit,
            'stat2_buy': stat2.buy,
            'purchase_ratio1': purchase_ratio1,
            'purchase_ratio2': purchase_ratio2,
            'conversion_rate1': purchase_ratio1*100,
            'conversion_rate2': purchase_ratio2*100
        }
        return render(request, 'statistics.html', context)
