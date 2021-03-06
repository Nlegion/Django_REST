"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pathlib import Path

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.urls import *
from rest_framework.permissions import AllowAny
from rest_framework.authtoken import views
from authors.views import AuthorModelViewSet, ArticleModelViewSet, BiographyModelViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
# router.register('article', ArticleModelViewSet, basename='articlev')
router.register('biography', BiographyModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='library',
        default_version='1.0',
        description='Some description',
    ),
    public=True,
    permission_classes=(AllowAny,)
)

# BASE_DIR = Path(__file__).resolve().parent.parent
# index = BASE_DIR / 'frontend/build/index.html'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'^api/(?P<version>\d\.\d)/authors/$', AuthorModelViewSet.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('^swagger(?P<format>\d\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
