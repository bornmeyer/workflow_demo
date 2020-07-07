from rest_framework import viewsets
from rest_framework.response import Response
from app.serializers.comment_serializer import CommentSerializer
from app.models.workflow import Workflow
from app.models.comment import Comment

"""
    Provides methods to manipulate comment resources, 
    accessible via /workflows/{workflow_id}/comments

    A get returns a list of all comments for the workflow,

    A post creates a new comment for the workflow

    A patch at /workflows/{workflow_id}/comments/{id} updates the comment

    A delete at /workflows/{workflow_id}/comments/{id} deletes the comment
"""
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request, workflow_pk=None):
        workflow = Workflow.objects.get(id=workflow_pk)
        comments = workflow.comment_set.all()
        response = self.serializer_class(comments, many=True).data
        return Response(data=response, status=200)

    def retrieve(self, request, pk=None, workflow_pk=None):
        workflow = Workflow.objects.get(id=workflow_pk)
        comment = workflow.comment_set.get(id=pk)
        response = self.serializer_class(comment).data       
        return Response(data=response, status=200)

    def create(self, request, workflow_pk=None):
        workflow = Workflow.objects.get(id=workflow_pk)
        new_comment = Comment(author=request.user, workflow=workflow)        
        new_comment.text = request.data['text']
        new_comment.save()
        response = self.serializer_class(new_comment).data
        return Response(data=response, status=201)
        