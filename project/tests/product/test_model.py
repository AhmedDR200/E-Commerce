from product.models import *
import pytest


pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_string_method(self, category_factory):
        # Arrage
        
        # Act
        x = category_factory()
        # Assert
        assert x.__str__() == "test_category"


class TestBrandModel:
    def test_string_method(self, brand_factory):
        # Arrage
        
        # Act
        x = brand_factory()
        # Assert
        assert x.__str__() == "test_brand"


class TestProductModel:
    def test_string_method(self, product_factory):
        # Arrage
        
        # Act
        x = product_factory()
        # Assert
        assert x.__str__() == "test_product"        