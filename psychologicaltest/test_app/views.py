from django.shortcuts import render

from register.models import User
from test_app.models import Userscore


def testdemo(request):
    if request.method == 'GET':
        return render(request,'test_demo.html')
    else:
        score = int(request.POST.get('total'))
        username = request.session.get('username', '未知用户')
        Userscore.objects.create(name=username,score=score)
        return render(request,'end.html',{'score':score})