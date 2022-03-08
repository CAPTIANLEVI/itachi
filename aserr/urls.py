from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from aserr import views


app_name='aserr'
urlpatterns=[
    path('home/',views.home)
]