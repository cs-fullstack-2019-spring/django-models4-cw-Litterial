from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Child
from .models import Mom

def index(request): #home page
    return HttpResponse("What's up?")
def children(request): #returns children then mom by child
    childfirst=Child.objects.all()  #array of children
    for x in childfirst:
        print(f'Child:{x.f_name} {x.l_name}') #Child
        print(f'Mom:{x.child_mom}') #Mom by Child
        print('\n')
    return HttpResponse()
def moms(request): #returns mom then child by Mom
    allMoms=Mom.objects.all() #array of moms
    for x in allMoms:
        print(f'Mom:{x.f_name} {x.l_name}') #Mom
        for y in Child.objects.filter(child_mom__f_name=x.f_name): #if the id matches the mom's name, return the child's name#
            print(f'Child:{y.f_name}')
    return HttpResponse()
def addchild(request): #adds new children to a mom
    allMoms=Mom.objects.all()
    def child1():
        newChild1= Child(f_name="Redd",l_name="Foxx",child_mom= allMoms[0] )
        newChild1.save()
        return HttpResponse(newChild1)
    def child2():
        newChild2= Child(f_name="Freddie",l_name="Mercury",child_mom= allMoms[1])
        newChild2.save()
        return HttpResponse(newChild2)
    def child3():
        newChild3= Child(f_name='Jim',l_name="Carrey",child_mom= allMoms[2])
        newChild3.save()
        return HttpResponse(newChild3)
    #calls each function
    child1()
    child2()
    child3()
    print(Child.objects.all())
    return HttpResponse()
def deletemom(request): #deletes the first mom
    allMoms=Mom.objects.all()
    allMoms[0].delete()
    return HttpResponse()

