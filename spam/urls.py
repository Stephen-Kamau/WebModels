
from django.urls import path
from django.conf.urls import include , url
from . import views


urlpatterns = [
    path('', views.Home , name = "spamHome"),
    path('spamming/', views.spam , name = "spamdata"),
    path("spamming/getspam/" , views.getSpam , name = 'getspam')

]
