from django.urls import path
from .views import RegisterView, UserViewSet, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('get-token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('verify-token/', verify_jwt_token),
]

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})