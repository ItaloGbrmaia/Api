
from django.contrib import admin
from django.urls import path, include

# from rest_framework import routers
# from app.api.viewsets import UserViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app.urls import user_urls
# route = routers.DefaultRouter()
# route.register(r'User', UserViewSet, basename="User")
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(route.urls)),
    path('', include(user_urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    
]


"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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