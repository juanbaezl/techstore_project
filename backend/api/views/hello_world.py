from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


class HelloWorldView(ViewSet):
    def list(self, request):
        return Response(
            {"message": "Hello World from Dockerized Django!"},
            status=status.HTTP_200_OK,
        )
