from django.urls import path
from . import views

# URLConf
urlpatterns = [
    #not calling function (), just calling reference
    path('hello/', views.say_hello)
]