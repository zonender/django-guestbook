from django.urls import path
from . import views # the . means from the same package.


urlpatterns = [
    path('hello/', views.index, name='index')
]