from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^events/', views.allEvents, name='all_events'),
    url(r'^new-event/', views.createEvent, name='create_event'),
    url(r'^event/(?P<pk>\d+)/attend/', views.attend_event, name='attend_event'),
    url(r'^edit/(?P<pk>\d+)', views.updateEvent, name='update_event'),
    url(r'^delete/(?P<pk>\d+)', views.deleteEvent, name='delete_event'),
    url(r'^my-event/', views.myEvents, name='my_events'),
    url(r'^joinUser/', views.joinUser, name='join-User-in-event'),
]
