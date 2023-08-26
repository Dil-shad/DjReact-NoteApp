from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def getRoutes(request):
    response_data = {'message': 'our api'}
    return Response(response_data)


@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getNote(request,pk):
    note=Note.objects.get(id=pk)
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request,pk):
    data=request.data
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(instance=note,data=data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)    

