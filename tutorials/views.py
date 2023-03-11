from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):

@api_view(['GET','PUT','DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = tutorial.objects.get(pk-pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'mesage': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def tutorial_list_published(request):
    # GET all published tutorials