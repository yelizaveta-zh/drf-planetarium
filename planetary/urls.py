from django.urls import path, include
from rest_framework.routers import DefaultRouter

from planetary.views import (
    AstronomyShowViewSet,
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
    ShowSessionViewSet,
    ReservationViewSet,
    TicketViewSet,
)

router = DefaultRouter()
router.register("astronomy_shows", AstronomyShowViewSet)
router.register("show_themes", ShowThemeViewSet)
router.register("planetarium_domes", PlanetariumDomeViewSet)
router.register("show_sessions", ShowSessionViewSet)
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "planetary"
