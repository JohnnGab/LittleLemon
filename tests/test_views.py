from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a test client for making API requests
        self.client = APIClient()
        
        # Create test instances of the Menu model
        self.menu_item = Menu.objects.create(title="Coffee", price=5, inventory=50)
        

    def test_getall(self):
        # Define the URL for the Menu list view
        url = reverse('menu-list')
        
        # Make a GET request to retrieve all Menu objects
        response = self.client.get(url)
        
        # Retrieve all Menu objects from the database
        menus = Menu.objects.all()
        
        # Serialize the retrieved objects using the MenuSerializer
        serializer = MenuSerializer(menus, many=True)
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the serialized data in the response equals the serialized data of all Menu objects
        self.assertEqual(response.data, serializer.data)
        