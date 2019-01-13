"""AmazonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from rest_framework_jwt.views import obtain_jwt_token
from apps.users.views import UserViewset, RoleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from users import views_base
from django.conf.urls import url, include

router = DefaultRouter()
router.register(r'api/users', UserViewset, base_name="users")
router.register(r'api/roles', RoleViewSet, base_name="roles")

schema_view = get_swagger_view(title='ShopVue API文档 ')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    path('apidoc/', schema_view),
    path('docs/', include_docs_urls(title='ShopVue 文档')),
    re_path('api/user/info/$', views_base.get_user_info),
    path('api/user/login', obtain_jwt_token),
    #re_path('api/goods/list', role_list, name= "角色列表")

]

