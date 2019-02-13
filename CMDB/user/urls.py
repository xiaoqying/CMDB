from django.conf.urls import url,include
from user import views

urlpatterns = [
    url(r'',views.User.as_view()),
    url(r'^add/',views.add.as_view()),
    url(r'^update/(\d+)/',views.update.as_view()),
    url(r'delete',views.delete.as_view()),
]