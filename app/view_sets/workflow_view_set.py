from rest_framework import viewsets, status
from rest_framework.response import Response

from app.serializers.workflow_serializer import WorkflowSerializer
from app.models.workflow import Workflow
from app.models.step import Step

class WorkflowViewSet(viewsets.ModelViewSet):
    serializer_class = WorkflowSerializer
    queryset = Workflow.objects.all()

    def create(self, request):
        steps = request.data.pop('steps')
        
        new_workflow = Workflow()
        new_workflow.author = request.user
        new_workflow.name = request.data['name']
        new_workflow.description = request.data['description']
        new_workflow.save()
        for i, step in enumerate(steps):
            step = Step.objects.create(**step, workflow=new_workflow, order=i)
        return Response(status=status.HTTP_201_CREATED)