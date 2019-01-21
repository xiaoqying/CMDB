from django.conf.urls import url,include
from django.contrib import admin
from salt import views

urlpatterns = [
    url(r'',views.apilist.as_view()),

]