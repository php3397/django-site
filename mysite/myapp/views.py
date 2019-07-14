from django.shortcuts import render


def getinfo(requests):
    return render(requests,'myapp/getinfo.html',{'title':'get info'})
