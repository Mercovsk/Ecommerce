from django.urls import path

from . import views

app_name ='item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('new_item/', views.new_item, name='new_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
]
