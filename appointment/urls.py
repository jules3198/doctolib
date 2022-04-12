from django.urls import path
from . import views
app_name = 'appointment'
urlpatterns = [
 path('next', views.next, name='next'),
 path('past', views.past, name='past'),
 path('search', views.search, name='search'),
 path('take-appointment/<int:id>', views.take_appointment, name='take-appointment'),
 path('appointment-manager', views.appointment_manager, name='appointment-manager'),
 path('validate-doctor', views.validateDoctor, name='validate-doctor'),
 path('appointment-delete/<int:id>', views.appointment_delete, name='appointment-delete'),
]