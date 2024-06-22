from fastapi.testclient import TestClient
from http import HTTPStatus
import pytest

from mlops_study.api import api


@pytest.fixture()
def client():
    return TestClient(api)


def test_root_returns_html_page(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert "<html>" in response.text
