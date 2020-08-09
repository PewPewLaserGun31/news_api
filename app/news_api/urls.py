from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("news", views.NewsPostViewSet)
router.register("comments", views.CommentViewSet)

urlpatterns = [path("", include(router.urls))]
