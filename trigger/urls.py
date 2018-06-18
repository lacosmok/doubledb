from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.EventList.as_view(), name='index'),
    path(r'full/', views.FullEventList.as_view(), name='full-list'),
    path(r'create/event/', views.CreateEvent.as_view(), name='create-event'),
    path(r'edit/event/<int:pk>', views.EditEvent.as_view(), name='edit-event'),

]