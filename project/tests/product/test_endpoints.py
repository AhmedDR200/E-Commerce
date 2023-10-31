import pytest

pytestmark = pytest.mark.django_db

# class TestCategoryEndpoints:
#     endpoint = '/api/category/'
    
#     def test_get(self, category_factory, api_client):
#         # Arrange
#         category_factory()
#         # Act
#         response = api_client().get(self.endpoint)
#         # Assert
#         assert response.status_code == 200




# class TestBrandEndpoints:
#     endpoint = '/api/brand/'
#     def test_get(self, client):
#         response = client.simulate_request(method='GET', path=self.endpoint)
#         assert response.status_code == 200


# class TestProductEndpoints:
#     endpoint = '/api/product/'
#     def test_get(self, client):
#         response = client.simulate_request(method='GET', path=self.endpoint)
#         assert response.status_code == 200
        