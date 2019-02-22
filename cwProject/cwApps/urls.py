from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('children/',views.children,name='children'),
    path('moms/',views.moms,name='moms'),
    path('addchild/',views.addchild,name='addchild'),
    path('deletemom/',views.deletemom,name='deletemom'),

]