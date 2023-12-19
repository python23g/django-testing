from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.forms import model_to_dict
from django.contrib.auth import authenticate
from base64 import b64decode
import json
from .models import Animal
from .serializers import AnimalSerializer



class LoginView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        return Response({"message": "you are loged in."}, status=status.HTTP_200_OK)


class AnimalsView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        animals = AnimalSerializer(Animal.objects.all(), many=True)

        return Response({'animals': animals.data}, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = AnimalSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
