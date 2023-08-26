from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Note
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def getRoutes(request):
    response_data = {'message': 'our api'}
    return Response(response_data)


@api_view(['POST'])
def createNote(request):
    serializer = NoteSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-created')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = get_object_or_404(Note, id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = get_object_or_404(Note, id=pk)
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = get_object_or_404(Note, id=pk)
    note.delete()
    return Response('Note deleted')
