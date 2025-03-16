import pytest
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from planetary.models import (
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Reservation,
)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user():
    return get_user_model().objects.create_user(
        username="testuser",
        password="testpass"
    )


@pytest.fixture
def auth_client(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    return api_client


@pytest.mark.django_db
def test_astronomy_show_list(api_client):
    AstronomyShow.objects.create(title="Black Holes", description="A journey through space")
    url = reverse("astronomyshow-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert any(item["title"] == "Black Holes" for item in response.data)


@pytest.mark.django_db
def test_astronomy_show_create_unauthenticated(api_client):
    url = reverse("astronomyshow-list")
    data = {"title": "Exoplanets", "description": "Discovering new worlds"}
    response = api_client.post(url, data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_astronomy_show_create_authenticated(auth_client):
    url = reverse("astronomyshow-list")
    data = {"title": "Exoplanets", "description": "Discovering new worlds"}
    response = auth_client.post(url, data)
    assert response.status_code == 201
    assert response.data["title"] == "Exoplanets"


@pytest.mark.django_db
def test_reservation_list_requires_auth(api_client):
    url = reverse("reservation-list")
    response = api_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_reservation_create(auth_client, test_user):
    url = reverse("reservation-list")
    response = auth_client.post(url, {})
    assert response.status_code == 201
    assert response.data["user"] == test_user.id


@pytest.mark.django_db
def test_ticket_create(auth_client, test_user):
    dome = PlanetariumDome.objects.create(name="Main Dome", rows=10, seats_in_row=20)
    show = AstronomyShow.objects.create(title="Galaxies", description="Deep space exploration")
    session_time = timezone.now() + timedelta(days=1)
    session = ShowSession.objects.create(
        astronomy_show=show, planetarium_dome=dome, show_time=session_time
    )
    reservation = Reservation.objects.create(user=test_user)
    url = reverse("ticket-list")
    data = {
        "row": 5,
        "seat": 10,
        "show_session": session.id,
        "reservation": reservation.id
    }
    response = auth_client.post(url, data)
    assert response.status_code == 201
    assert response.data["row"] == 5
    assert response.data["seat"] == 10
