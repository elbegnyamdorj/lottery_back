from django.urls import path

from . import views

urlpatterns = [
    path('', views.LotteryView.as_view(), name='index'),
    path('delete/', views.LotteryDelete.as_view(), name='delete'),
    path('<str:number>', views.LotteryChecker.as_view(), name='check'),

]