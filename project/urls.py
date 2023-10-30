from django.contrib import admin
from django.urls import path, include
from product import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', views.CategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
