from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import user_signup, user_login, user_logout

urlpatterns=[
    path('user_registration/',user_signup,name='user_signup'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]