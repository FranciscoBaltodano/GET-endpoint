from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view


@api_view(['GET','PUT','DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = tutorial.objects.get(pk-pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'mesage': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


@csrf_exempt 
def tutorials_api(request, id=0):
    if request.method=='GET':
        tutorials = Tutorial.objects.all()
        tutorials_serializer =  TutorialSerializer(tutorials, many = True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorials_serializer = TutorialSerializer(data = tutorial_data)
        if tutorials_serializer.is_valid():
            tutorials_serializer.save()
            return JsonResponse('Añadido Exitosamente!!!',safe=False)
        return JsonResponse("Fallo al intentar agregar", safe=False)
    elif request.method=='PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial = Tutorial.objects.get(id=tutorial_data['id'])
        tutorials_serializer = TutorialSerializer(tutorial, data=tutorial_data)
        if tutorials_serializer.is_valid():
            tutorials_serializer.save()
            return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
        return JsonResponse("Fallo al Actualizar")
    elif request.method=='DELETE':
        tutorial = Tutorial.objects.get(id=id)
        tutorial.delete()
        return JsonResponse('Eliminado Exitosamente', safe=False)