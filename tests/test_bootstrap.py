import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from apps.accounts.models import UserProfile


@pytest.mark.django_db
def test_anonymous_cannot_view_dashboard(client):
    response = client.get(reverse("dashboard"))
    assert response.status_code == 302
    assert reverse("login") in response.url


@pytest.mark.django_db
def test_authenticated_user_sees_real_role_label(client):
    user = get_user_model().objects.create_user("member", password="test-long-password-2026")
    UserProfile.objects.create(user=user, role=UserProfile.Role.MARKET)
    client.force_login(user)
    response = client.get(reverse("dashboard"))
    assert response.status_code == 200
    assert "市场人员" in response.content.decode("utf-8")
    assert "待 Codex 开发" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_dashboard_escapes_username(client):
    user = get_user_model().objects.create_user("<script>alert(1)</script>", password="test-long-password-2026")
    client.force_login(user)
    response = client.get(reverse("dashboard"))
    assert response.status_code == 200
    assert b"<script>alert(1)</script>" not in response.content
    assert b"&lt;script&gt;alert(1)&lt;/script&gt;" in response.content
