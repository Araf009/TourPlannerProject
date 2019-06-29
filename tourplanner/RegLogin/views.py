from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .forms import GuideRegInfoForm
from planner.models import GUIDE, USER, CITY
# Create your views here.

temp = None

def debug(s):
    print( "\n\n\n" + s + "\n\n\n" )

def index(request):
    template = loader.get_template('WebsiteFrontPage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register_guide(request):
    template = loader.get_template('RegistrationGuide.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register_user(request):
    template = loader.get_template('registrationUser.html')
    all_city = CITY.objects.all()
    context = {}
    city = []
    for e in all_city:
        city.append(e.city_name)
    city.sort()
    context['city'] = city
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('loginForm.html')
    context={}
    return HttpResponse(template.render(context, request))


def login_validation(request):
    template = loader.get_template('profile.html')
    email=request.POST['email']
    password=request.POST['pass']
    context={'email': email, 'password': password}
    a = USER.objects.filter( Email = email )
    b = GUIDE.objects.filter( Email = email )

    if a.count() == 1 and b.count() == 0 and a[0].Password == password :
        template = loader.get_template('profile.html')
        context = {}
        debug( str( a[0].pk ) )
        request.session['user'] = a[0].pk
        request.session.modified = True
        return HttpResponse(template.render(context, request))
    if b.count() == 1 and a.count() == 0 and b[0].Password == password :
        template = loader.get_template('profile.html')
        context = {}
        debug("b")
        temp = b[0].pk
        request.session['user'] = b[0].pk
        request.session.modified = True
        return HttpResponse(template.render(context, request))
    return HttpResponse("<h1> Invalid Credentials </h1>")



def guide_registration_data(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password=request.POST['password']
    email=request.POST['email']
    phoneNumber=request.POST['phoneNumber']
    address=request.POST['address']
    gender=request.POST['gender']
    retype_pass = request.POST['password_2']
    #about, image + some form validation required here
    a = GUIDE.objects.filter(Email=email)
    if a.count() > 0:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    if password != retype_pass:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    model=GUIDE(FirstName=first_name, LastName=last_name, Email=email,
                Password=password,Address=address, Contact=phoneNumber,Gender=gender)
    model.save()
    #return  render(request, 'RegistrationGuide.html')
    template = loader.get_template('profile.html')
    context = {'type': "guide", 'email': email, 'password': password}
    return HttpResponse(template.render(context, request))

def user_registration_data(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    retype_pass = request.POST['password_2']
    email = request.POST['email']
    phoneNumber = request.POST['phoneNumber']
    address = request.POST['address']
    gender = request.POST['gender']
    city = request.POST['city']
    a = USER.objects.filter(Email=email)

    if a.count() > 0:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    if password != retype_pass:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    model = USER(FirstName=first_name, LastName=last_name, Email=email, cityID = CITY.objects.filter( city_name = city )[0],
                  Password=password, Address=address, Contact=phoneNumber, Gender=gender)
    model.save()
    # return  render(request, 'RegistrationGuide.html')
    template = loader.get_template('profile.html')
    context = {'type': "user", 'email': email, 'password': password}
    return HttpResponse(template.render(context, request))



def display_user_edit_page(request):
    debug(str(request.session['user']))
    template = loader.get_template('EditUserProfile.html')
    a = USER.objects.filter( pk = request.session['user'])#request.session['user'] )
    context = {'FirstName' : a[0].FirstName,
               'LastName' : a[0].LastName,
               'Address' : a[0].Address,
               'Password' : a[0].Password
               }
    return HttpResponse(template.render(context, request))

def logout(request):
    del request.session['user']

def edit_user_save_changes(request):
    print( request.POST )
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    retype_pass = request.POST['password_2']
    address = request.POST['address']
    if password != retype_pass :
        return HttpResponse("<h1>Password didn't match</h1>")
    user_edit = USER.objects.get( id = request.session['user'] )
    user_edit.FirstName = first_name
    user_edit.LastName = last_name
    user_edit.Password = password
    user_edit.Address = address
    user_edit.save()
    template = loader.get_template('profile.html')
    context = {'FirstName': user_edit.FirstName,
               'LastName': user_edit.LastName,
               'Address': user_edit.Address,
               'Password': user_edit.Password
               }
    return HttpResponse(template.render(context, request))


