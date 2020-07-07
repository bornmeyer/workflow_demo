import uuid
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Workflow, User
from django.core.exceptions import ObjectDoesNotExist

class WorkflowEndpointTests(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        api_key = uuid.uuid4()
        User.objects.create(firstname="Max", lastname="Mustermann", email="max@mustermann.com", api_key=api_key)

    def test_that_you_can_create_a_workflow(self):
        data = {
            "name": "How to nail something",
            "description": "Basic instructions to nail something"
        }

        requesting_user = User.objects.get(email="max@mustermann.com")
        url = f"/workflows/?api_key={requesting_user.api_key}"
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(data.items() <= response.data.items())

    def test_that_you_can_update_a_workflow(self):
        workflow = Workflow.objects.create(name="not just a test", description="just a test")
        expected = "this is a tribute"
        data = {
            "name": expected
        }

        requesting_user = User.objects.get(email="max@mustermann.com")
        url = f"/workflows/{workflow.id}/?api_key={requesting_user.api_key}"
        response = self.client.patch(url, data, format='json')
        self.assertTrue(response.data['name'] == expected)

    def test_that_you_can_delete_a_workflow(self):
        workflow = Workflow.objects.create(name="not just a test", description="just a test")
        requesting_user = User.objects.get(email="max@mustermann.com")
        url = f"/workflows/{workflow.id}/?api_key={requesting_user.api_key}"
        response = self.client.delete(url, format='json')
        with self.assertRaises(ObjectDoesNotExist):
            Workflow.objects.get(id=workflow.id)

    def test_that_steps_are_created_if_provided_and_ordered(self):
        data = {
            "name": "How to nail something",
            "description": "Basic instructions to nail something",
            "steps": [
                {
                    "name": "Place nail",
                    "description": "Hold nail on top the thing to be nailed"
                },
                {
                    "name": "Hit nail",
                    "description": "Hit the nail repeatedly with a hammer"
                }   
            ]
        }

        requesting_user = User.objects.get(email="max@mustermann.com")
        url = f"/workflows/?api_key={requesting_user.api_key}"
        response = self.client.post(url, data, format='json')

        saved_workflow = Workflow.objects.get(id=response.data['id'])

        self.assertTrue(saved_workflow.step_set.all()[0].name == "Place nail")
        self.assertTrue(saved_workflow.step_set.all()[1].name == "Hit nail")