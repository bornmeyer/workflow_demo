from rest_framework import viewsets, status
from rest_framework.response import Response

from app.serializers.step_serializer import StepSerializer
from app.models.workflow import Workflow
from app.models.step import Step

class StepViewSet(viewsets.ModelViewSet):
    serializer_class = StepSerializer
    queryset = Step.objects.all()

    def list(self, request, workflow_pk=None):
        print(request.user.email)
        workflow = Workflow.objects.get(id=workflow_pk)
        steps = workflow.step_set.all()
        response = self.serializer_class(steps, many=True).data
        return Response(data=response, status=200)

    def retrieve(self, request, pk=None, workflow_pk=None):
        workflow = Workflow.objects.get(id=workflow_pk)
        step = workflow.step_set.get(id=pk)
        response = self.serializer_class(step).data
        return Response(data=response, status=200)