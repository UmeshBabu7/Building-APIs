
from django.contrib import admin
from django.urls import path,include,re_path
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('LittleLemonAPI/',include('LittleLemonAPI.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/blacklist/',TokenBlacklistView.as_view(),name='token_blacklist'),
]
