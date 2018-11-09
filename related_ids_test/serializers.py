from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField
from .models import Parent, Child

class ChildSerializer(DynamicModelSerializer):
  class Meta:
    model  = Child
    fields = '__all__'

class ParentSerializer(DynamicModelSerializer):
  class Meta:
    model  = Parent
    fields = '__all__'

  children = DynamicRelationField(ChildSerializer, many = True, deferred = True)
