from django.urls import path
from . import views
urlpatterns = [
 path('next', views.next, name='next'),
 path('past', views.past, name='past'),
]