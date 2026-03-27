from django.shortcuts import render, redirect

from register.models import User


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        name = request.POST.get('uname')
        sex = request.POST.get('gender')
        age = int(request.POST.get('uage'))
        User.objects.create(uname=name,usex=sex,uage=age)
        request.session['username'] = name
        return redirect('/test_app/testdemo/')