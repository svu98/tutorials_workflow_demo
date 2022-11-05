from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial

# Create your tests here.

# This test verity that when we reverse the view named home, we get the expected
# path for the homepage on the website, which is "/". 
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

# This test verifies a Tutorial object is successfully created in the database.
@pytest.mark.django_db
def test_create_tutorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"