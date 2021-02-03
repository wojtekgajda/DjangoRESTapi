from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'films', views.FilmViewSet, basename='FilmModel')
router.register(r'reviews', views.ReviewViewSet, basename='ReviewModel')
router.register(r'actors', views.ActorViewSet, basename='ActorModel')

urlpatterns = [
    url(r'^api-token-auth/', obtain_jwt_token),
    path('', include(router.urls)),

]
