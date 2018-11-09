from django.conf.urls import url, include
from dynamic_rest.routers import DynamicRouter
from .views import ParentViewSet, ChildViewSet

crud_router = DynamicRouter()

crud_router.register_resource(ParentViewSet)
crud_router.register_resource(ChildViewSet)

urlpatterns = [
  url(r'^crud/', include(crud_router.urls)),
]
