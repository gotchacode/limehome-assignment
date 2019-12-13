import requests
from rest_framework.test import RequestsClient
from django.test import TestCase, LiveServerTestCase
from django.urls import reverse

class TestHotelsAPI(LiveServerTestCase):
    def setUp(self):
        self.valid_coord = '52.5200,13.4050'
        self.invalid_coord = '51.9173,1000'
        self.client = RequestsClient()
        self.api_url = f"{self.live_server_url}{reverse('hotels:hotels-search-api')}"

    def test_hotels_api_correct_coord(self):
        final_api_url = f"{self.api_url}?at={self.valid_coord}"
        response = self.client.get(final_api_url)
        assert 'title' in response.json()[0].keys()
        assert 'position' in response.json()[0].keys()
        assert len(response.json()) > 0
        assert response.status_code == 200

    def test_hotels_api_incorrect_coord(self):
        final_api_url = f"{self.api_url}?at={self.invalid_coord}"
        response = self.client.get(final_api_url)
        assert len(response.json()) == 0
        assert response.status_code == 404
