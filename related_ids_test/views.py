from dynamic_rest.viewsets import DynamicModelViewSet
from .models import Parent, Child
from .serializers import ParentSerializer, ChildSerializer

class ChildViewSet(DynamicModelViewSet):
  queryset         = Child.objects
  serializer_class = ChildSerializer

class ParentViewSet(DynamicModelViewSet):
  queryset         = Parent.objects
  serializer_class = ParentSerializer
