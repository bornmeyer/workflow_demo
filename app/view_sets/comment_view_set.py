from rest_framework import viewsets, status
from rest_framework.response import Response

from app.serializers.comment_serializer import CommentSerializer
from app.models.workflow import Workflow
from app.models.step import Step
from app.models.comment import Comment

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Step.objects.all()

    def list(self, request, workflow_pk=None):
        workflow = Workflow.objects.get(id=workflow_pk)
        comments = workflow.comment_set.all()
        response = self.serializer_class(comments, many=True).data
        return Response(data=response, status=200)

    def retrieve(self, request, pk=None, workflow_pk=None):
        workflow = Workflow.objects.get(id=workflow_pk)
        comment = workflow.comments_set.get(id=pk)
        response = self.serializer_class(comment).data
        return Response(data=response, status=200)

    def create(self, request, workflow_pk=None):
        workflow = Workflow.objects.get(id=workflow_pk)
        new_comment = Comment(author=request.user, workflow=workflow)        
        new_comment.text = request.data['text']
        new_comment.save()
        response = self.serializer_class(new_comment).data
        return Response(data=response, status=201)
        