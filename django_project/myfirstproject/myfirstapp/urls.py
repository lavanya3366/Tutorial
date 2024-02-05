from django.urls import path
from . import views
urlpatterns=[
    path('',views.myfunctioncall,name="index"),
    path('about',views.myfunctionabout,name="about"),
    path('add/<int:a>/<int:b>',views.myfunctionadd,name="add"),
    path('intro/<str:name>/<int:age>',views.intro,name="intro"),
    path('myfirstpage',views.myfirstpage,name="myfirstpage"),
    path('mysecondpage',views.mysecondpage,name="mysecondpage"),
    path('mythirdpage',views.mythirdpage,name="mythirdpage"),
    path('imagepage',views.imagepage,name="imagepage"),
    path('imagepage2',views.imagepage2,name="imagepage2"),
    path('imagepage3',views.imagepage3,name="imagepage3"),
    path('imagepage4',views.imagepage4,name="imagepage4"),
     path('imagepage5/<str:imagename>',views.imagepage5,name="imagepage5"),
     path('myform',views.myform,name='myform'),
     path('submitmyform',views.submitmyform,name="submitmyform"),
    path('myform3',views.myform3,name='myform3')
]


