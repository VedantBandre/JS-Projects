from django.urls import path
from . import views

urlpatterns = [
    path('', views.pw_gen, name='pw_gen'),
]
