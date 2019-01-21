from django.conf.urls import url,include
from django.contrib import admin
from host import views

urlpatterns = [
    url(r'^hostpage/',views.hostpage.as_view()),
    url(r'^add/',views.add.as_view()),
    url(r'^update/(\d+)/',views.update.as_view()),
    url(r'delete',views.delete.as_view()),
    url(r'^search/',views.search.as_view()),
    url(r'^login/',views.login.as_view()),
    url(r'^logout/',views.logout.as_view()),
    url(r'^register/',views.register.as_view()),
]