from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowAllStd, name='all_std'),
    path('add/', views.AddStd, name='add'),
    path('update/<str:pk>/', views.UpdateStd, name='update'),
    path('delete/<str:pk>/', views.DeleteStd, name='delete'),
]
