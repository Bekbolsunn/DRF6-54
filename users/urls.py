from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from users.views import (
    RegistrationAPIView,
    AuthorizationAPIView,
    ConfirmUserAPIView,
    CustomTokenObtainPairView
)
from users.oauth import GoogleLoginAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('authorization/', AuthorizationAPIView.as_view()),
    path('confirm/', ConfirmUserAPIView.as_view()),

    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('google-login/', GoogleLoginAPIView.as_view()),
]