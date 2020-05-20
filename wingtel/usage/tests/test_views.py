from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ExceededSubsListAPIView(APITestCase):

# Test response status code.
    def test_list_exceeded(self):
        url = reverse('exceeded') + '?exceeded=10/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
