from rest_framework import viewsets, status
from rest_framework.response import Response

from app.serializers.workflow_serializer import WorkflowSerializer
from app.models.workflow import Workflow
from app.models.step import Step

"""
    Provides methods to manipulate workflow resources, accessible via /workflows

    A get returns a list of all workflows,

    A post creates a new workflow

    A patch at /workflows/{id} updates the workflow

    A delete at /workflows/{id} deletes the workflow
"""
class WorkflowViewSet(viewsets.ModelViewSet):
    serializer_class = WorkflowSerializer
    queryset = Workflow.objects.all()

    def create(self, request):
        new_workflow = Workflow()
        new_workflow.author = request.user
        new_workflow.name = request.data['name']
        new_workflow.description = request.data['description']
        new_workflow.save()
        if 'steps' in request.data:
            steps = request.data.pop('steps')
            for i, step in enumerate(steps):
                step = Step.objects.create(**step, workflow=new_workflow, order=i)
        return Response(data=self.serializer_class(new_workflow).data, status=status.HTTP_201_CREATED)