from pytest_factoryboy import register
from .factories import *

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
