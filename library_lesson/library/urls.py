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
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from authors.views import *

router = SimpleRouter()
# router.register('authors', AuthorModelViewSet)
# router.register('books', BookModelViewSet)
# router.register('biography', BiographyModelViewSet)
router.register('article', ArticleModelViewSet, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/article-list-veiw', ArticleModelViewSet.as_view({'get':'list'})),
    path('api/article-list-veiw/kwargs', ArticleModelViewSet.as_view({'get': 'list'})),

    ]
# path('api/article-veiw', ArticleModelView()),
# path('api/article-veiw', article_view),
#     path('api/article-list-veiw', ArticleListModelView.as_view()),
#     path('api/article-create-veiw', ArticleCreateModelView.as_view()),
#     path('api/article-create-veiw/<int:pk>', ArticleCreateModelView.as_view()),
# ]
