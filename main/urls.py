from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kill/<int:pid>', views.process_kill, name='pkill')
]