import uuid
from rest_framework.test import APITestCase
from app.models import Workflow, User, Comment

class CommentEndpointTests(APITestCase):
    def setUp(self):
        User.objects.all().delete()
        api_key = uuid.uuid4()
        self.user = User.objects.create(firstname="Max", lastname="Mustermann", email="max@mustermann.com", api_key=api_key)
        self.workflow = Workflow.objects.create(name="test", description="test")
        

    def test_that_you_can_create_a_comment(self):
        url = f"/workflows/{self.workflow.id}/comments/?api_key={self.user.api_key}"
        expected = "Lorem ipsum dolor sit amet."

        response = self.client.post(url, {'text': expected}, format='json')
        self.workflow.refresh_from_db()

        assert len(self.workflow.comment_set.all()) == 1
        assert self.workflow.comment_set.all()[0].text == expected
        assert response.status_code == 201

    def test_that_you_can_delete_a_comment(self):
        self.workflow.comment_set.create(text="just a test", author=self.user)
        comment_id = self.workflow.comment_set.all()[0].id

        url = f"/workflows/{self.workflow.id}/comments/{comment_id}/?api_key={self.user.api_key}"

        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.workflow.comment_set.count(), 0)

    def test_that_you_can_patch_a_comment(self):
        comment = self.workflow.comment_set.create(text="just a test", author=self.user)
        expected = 'test123455'
        comment_id = self.workflow.comment_set.all()[0].id

        url = f"/workflows/{self.workflow.id}/comments/{comment_id}/?api_key={self.user.api_key}"

        response = self.client.patch(url, {'text': expected}, format='json')
        comment.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected, comment.text)

    def test_that_you_can_get_all_comments(self):
        self.workflow.comment_set.create(text="just a test", author=self.user)
        self.workflow.comment_set.create(text="just a test", author=self.user)
        url = f"/workflows/{self.workflow.id}/comments/?api_key={self.user.api_key}"

        response = self.client.get(url, format='json')

        self.assertEqual(len(response.data), 2)

    def test_that_you_can_get_a_specific_comment(self):        
        self.workflow.comment_set.create(text="just a test", author=self.user)
        comment = self.workflow.comment_set.create(text="just a test", author=self.user)

        url = f"/workflows/{self.workflow.id}/comments/{comment.id}/?api_key={self.user.api_key}"

        response = self.client.get(url, format='json')

        self.assertEqual(response.data['id'], str(comment.id))