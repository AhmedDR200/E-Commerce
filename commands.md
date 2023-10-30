# Packages
- Django
- Django-RestFramework
- Python-dotenv
- Pytest
- Pytest-django
- Black
- Django-mptt
- drf-spectacular
- coverage
- pytest-cov


for creating secret keys in python shell:

    from django.core.management.utils import get_random_secret_key
    
    print(get_random_secret_key())


for creating schema:

    python manage.py spectacular --file schema.yml