from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_auth.views import LoginView, LogoutView

from .views import *

router = DefaultRouter()
router.register(r'interests', InterestViewSet)
router.register(r'regions', RegionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
