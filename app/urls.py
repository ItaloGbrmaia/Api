from rest_framework.routers import DefaultRouter
from django.urls import path 
from app.api.viewsets import UserViewSet


router = DefaultRouter()

router.register(r'', UserViewSet, basename='user')

user_urls = router.urls