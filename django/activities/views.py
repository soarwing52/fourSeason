from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import permissions, viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format)
    })


class ActivityViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permision_classes = [permissions.IsAuthenticated, ]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        