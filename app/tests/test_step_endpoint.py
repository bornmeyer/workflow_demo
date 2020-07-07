import uuid
from rest_framework.test import APITestCase
from app.models import Workflow, User, Step

class StepEndpointTests(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        api_key = uuid.uuid4()
        self.user = User.objects.create(firstname="Max", lastname="Mustermann", email="max@mustermann.com", api_key=api_key)
        self.workflow = Workflow.objects.create(name="test", description="test")
        self.workflow.step_set.create(name="test", description="test", order=0)
        self.step = self.workflow.step_set.create(name="test2", description="test2", order=1)

    def test_that_you_can_get_all_steps(self):
        url = f"/workflows/{self.workflow.id}/steps/?api_key={self.user.api_key}"
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_that_you_can_get_a_specific_step(self):
        url = f"/workflows/{self.workflow.id}/steps/{self.step.id}/?api_key={self.user.api_key}"

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "test2")