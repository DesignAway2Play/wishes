from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_item',
         views.add_item, name='add_item'),
    path('<int:pk>/delete/',
         views.ItemDelete.as_view(), name='ItemDelete'),
]
