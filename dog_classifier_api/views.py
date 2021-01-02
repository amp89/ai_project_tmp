from django.shortcuts import render
from rest_framework.views import APIView
from view_classes import APIAuthView
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from .model_wrapper import classify_dog

from django.conf import settings
# Create your views here.


class HealthCheckView(APIView):
    def get(self, request):
        return Response({},status=status.HTTP_200_OK)

class AuthHealthCheckView(APIAuthView):
    def get(self, request):
        return Response({},status=status.HTTP_200_OK)


class DogClassifierView(APIAuthView):

    # parser_classes = [FileUploadParser,]

    def post(self, request, *args, **kwargs):
        # file_obj = request.data['file']
        
        # print(request.FILES)

        if len(request.FILES) != 1:
            return Response({'message":"One file required. Only uplaod one file.'}, status=status.HTTP_400_BAD_REQUEST)

        
        file_name, file_obj = next(request.FILES.items())

        if len(file_obj) > settings.DOG_CLASSIFIER_API_MAX_UPLOAD_BYTES:
            return Response({'message":"Files cannot be larger than 10 mb'}, status=status.HTTP_400_BAD_REQUEST)


        breed, probability = classify_dog(file_obj.read())

        return Response({"breed":breed, "probability": probability}, status=status.HTTP_200_OK)

