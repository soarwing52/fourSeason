from django.urls import path, include
from activities import views
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'activities', views.ActivityViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.api_root),
    # path('activities', views.ActivityList.as_view(), name='activity-list'),
    # path('<int:pk>/', views.ActivityDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]

activity_list = ActivityViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = ActivityViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})