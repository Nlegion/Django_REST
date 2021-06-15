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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.urls import *
from users.views import UserModelViewSet, CustomUserModelViewSet, UserModelViewSet1, UserModelViewSet2
from TODO.views import ProjectModelViewSet, TODOViewSet
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

schema_view = get_schema_view(
    openapi.Info(
        title='library',
        default_version='1.0',
        description='Some description',
    ),
    public=True,
    permission_classes=(AllowAny,)
)

router = DefaultRouter()
router.register('users', UserModelViewSet)
# router.register('users_1', UserModelViewSet1)
# router.register('users_2', UserModelViewSet2)
router.register('Project', ProjectModelViewSet)
router.register('ToDo', TODOViewSet)

filter_router = DefaultRouter()
filter_router.register('title', ProjectModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('filters/', include(filter_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(r'^api/(?P<version>\d\.\d)/users/$', CustomUserModelViewSet.as_view({'get': 'list'})),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('^swagger(?P<format>\d\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
