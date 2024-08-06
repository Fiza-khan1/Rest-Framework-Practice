from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from .views import modelViewSet, RegisterUser
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



router = DefaultRouter()
router.register(r'itemss', modelViewSet)
router.register(r'UserRegis', RegisterUser)

from django.views.generic import TemplateView
urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui')
  
 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)