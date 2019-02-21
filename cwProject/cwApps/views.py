from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Child
from .models import Mom

def index(request):
    return HttpResponse("What's up?")
def children(request):
    #listofchildren=''
    childfirst=Child.objects.all()
    allMoms=Mom.objects.all()
    print(childfirst)
    for x in childfirst:
        print(f'{x.f_name} {x.l_name}')
        for y in Child.objects.filter(child_mom__f_name=x.f_name):
            print(y.f_name)
    return HttpResponse()
