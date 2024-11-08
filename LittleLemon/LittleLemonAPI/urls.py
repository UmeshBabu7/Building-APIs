from django.urls import path
from .import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu_items/',views.menu_items),
    path('menu_item/<int:id>/',views.single_item),
    path('secret/',views.secret),
    path('api-token-auth/',obtain_auth_token),
    path('manager-view/',views.manager_view),
    path('throttle-check/',views.throttle_check),
    path('throttle-check-auth/',views.throttle_check_auth),
    path('me/',views.me),
    path('group/manager/users',views.manager)

    
]
