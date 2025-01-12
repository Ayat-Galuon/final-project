import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from base.models import Product
from rest_framework.authtoken.models import Token #add
from django.contrib.auth.models import User       #add

def create_product():
  return Product.objects.create(
        name=" Product Name ",
        price=0,
        brand="Sample brand ",
        countInStock=0,
        category="Sample category",
        description=" ")



# Test for getting the product list
def test_api_product_list():
    client = APIClient()
    response = client.get("/api/products/")
    assert response.status_code == 200


# # Test for getting a single product by ID
# def test_api_product_retrieve():
#     client = APIClient()
#     response = client.get("/api/products/1/")
#     assert response.status_code == 200


# # Test for updating a product
# def test_api_product_update():
#     client = APIClient()
#     updated_data = {
#         "name": "Updated Product",
#         "description": "Updated description",
#         "price": 29.99,
#         "quantity": 150
#     }
#     response = client.put("/api/products/1/", updated_data, format="json")
#     assert response.status_code == 200

# # Test for deleting a product
# def test_api_product_delete():
#     # Step 1: Set up the test client
#     client = APIClient()

#     # Step 2: Create a product to ensure that the DELETE request is valid
#     product = Product.objects.create(name="Test Product", price=100)  # Create a product instance

#     # Step 3: Try to delete the product with the valid ID
#     response = client.delete(f"/api/products/{product.id}/")  # Make sure URL is correct

#     # Step 4: Print the response content for debugging
#     print(response.content)  # This will print the error message or response data

#     # Step 5: Assert the correct status code (204 for successful deletion)
#     assert response.status_code == 204, f"Expected 204, got {response.status_code}"

#     # Step 6: Verify that the product is deleted from the database
#     product_exists = Product.objects.filter(id=product.id).exists()
#     assert not product_exists, "Product was not deleted from the database"

# # Test for invalid product creation due to missing data
# def test_api_product_creation_invalid():
#     client = APIClient()
#     response = client.post("/api/products/create/", {
#         "description": "Invalid product",
#         "price": 15.99,
#         "quantity": 50
#     }, format="json")

#     assert response.status_code == 400
