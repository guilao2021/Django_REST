from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tabela_precos.views import TratamentosViewSet

router = routers.DefaultRouter()
router.register('tratamentos', TratamentosViewSet, basename='Tratamentos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    ]
