from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

class CategoryTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.access_token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))

    def test_create_category(self):
        example_data = {
            "name": "Category",
            "description": "Description",
            "category_code": "Category",
            # "image": "media/category/portfolio-details-1.jpg"
        }
        response = self.client.post("/api/category/", example_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_category_list(self):
        response = self.client.get("/api/category/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)