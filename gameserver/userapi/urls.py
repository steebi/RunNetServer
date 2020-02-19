from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import HelloView, PlayerViewSet

urlpatterns = [
    path('userlogin/', obtain_auth_token, name='token_login'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('create-user/', PlayerViewSet.as_view(), name='createUser')
]