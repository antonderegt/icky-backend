from django.test import TestCase
from .models import Problem

class ProblemModelTest(TestCase):
    """Test Problem Model"""

    def setUp(self):
        Problem.objects.create(problem="test", description="test desc", createdAt="2020")

    def test_problem_creation(self):
        problem = Problem.objects.get(problem='test')
        self.assertEqual(problem.get_description(), "test desc")

import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .serializers import ProblemSerializer

# initialize the APIClient app
client = Client()
