from app.view_sets import UserViewSet, WorkflowViewSet, StepViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

def create_router():
    router = DefaultRouter()
    router.register(r'users', UserViewSet, basename='user')
    router.register(r'workflows', WorkflowViewSet, basename='workflow')

    nested_router = routers.NestedSimpleRouter(router, r'workflows', lookup='workflow')
    nested_router.register('steps', StepViewSet, basename='step')
    nested_router.register('comments', CommentViewSet, basename='comment')

    urlpatterns = router.urls + nested_router.urls
    return router, urlpatterns