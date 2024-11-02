from django.urls import path
from .import views

urlpatterns = [
    path('menu_items/',views.menu_items),
    path('menu_item/<int:id>/',views.single_item)
    
]
