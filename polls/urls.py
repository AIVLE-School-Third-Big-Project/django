
from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),        
]

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('', views.IndexView, name='index123'),        
]