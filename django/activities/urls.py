from django.urls import path, include
from activities import views
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

activity_list = ActivityViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
activity_detail = ActivityViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

