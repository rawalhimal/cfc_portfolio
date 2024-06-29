from django.urls import path
from .views import index,component
urlpatterns = [
    path('',index,name = "index"),
    path('comp/',component, name = "component")
]
