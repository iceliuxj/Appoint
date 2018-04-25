from django.conf.urls import url
from . import views 

urlpatterns =[
	url(r'^$', views.index), # login page
    url(r'^login/0$', views.login), # POST _ Login
    url(r'^register$', views.registerpage),
	url(r'^register/0$', views.register),
    url(r'^homepage$', views.homepage),
    url(r'^userpage$', views.userpage),
    url(r'^acceptpopup.html$', views.acceptpopup),
    url(r'^rejectpopup.html$', views.rejectpopup),
    url(r'^addschedule.html$', views.addschedule),
    url(r'^homepage/addshedule$', views.addschedules),
]
