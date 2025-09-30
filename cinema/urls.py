from django.urls import path, include
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          genre_list,
                          genre_detail,
                          ActorList,
                          ActorDetail,
                          CinemaHallList,
                          CinemaHallDetail)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", genre_list, name="genre_list"),
    path("genres/<int:pk>/", genre_detail, name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("cinema_halls/", CinemaHallList.as_view(), name="cinema_list"),
    path("cinema_halls/<int:pk>/",
         CinemaHallDetail.as_view(),
         name="cinema_detail"),
]

app_name = "cinema"
