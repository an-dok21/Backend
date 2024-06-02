from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('confirm/<str:token>/', views.confirm_subscription, name='confirm_subscription'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]