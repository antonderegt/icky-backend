from django.test import TestCase
from .models import Problem

def create_problem(name, desc):
    return Problem.objects.create(problem=name, description=desc)

class ProblemModelTest(TestCase):
    """
    Test Problem Model
    """

    def setUp(self):
        create_problem("test", "test desc")

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

class GetProblemsTest(TestCase):
    """
    Test module for GET all problems API
    """

    def setUp(self):
        self.p1 = create_problem("aa test 1", "test 1 desc")
        self.p2 = create_problem("bb test 2", "test 2 desc")

    def test_get_all_problems(self):
        # get API response
        response = client.get(reverse('get_post_problems'))
        # get data from db
        problems = Problem.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_problem(self):
        response = client.get(reverse('get_delete_update_problem', kwargs={'pk': self.p1.pk}))
        problem = Problem.objects.get(pk=self.p1.pk)
        serializer = ProblemSerializer(problem)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
    
    def test_get_invalid_single_problem(self):
        response = client.get(reverse('get_delete_update_problem', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProblemTest(TestCase):
    """ Test module for inserting a new problem """

    def setUp(self):
        self.valid_payload = {
            'problem': 'New Problem',
            'description': 'Desc of new problem'
        }
        self.invalid_payload = {
            'problem': '',
            'description': 'White'
        }

    def test_create_valid_problem(self):
        response = client.post(
            reverse('get_post_problems'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_problem(self):
        response = client.post(
            reverse('get_post_problems'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
