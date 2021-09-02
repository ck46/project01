from django.http import HttpResponse

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from digestai.models import StudySet
from digestai.serializers import StudySetSerializer
from rest_framework.decorators import api_view


# API views
@api_view(['GET', 'POST', 'DELETE'])
def studyset_list(request):
    # GET list of studysets, post a new studyset, delete all studysets
    if request.method == 'GET':
        studysets = StudySet.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            studysets = tutorials.filter(title_icontains=title)

        studysets_serializer = StudySetSerializer(studysets, many=True)
        return JsonResponse(studysets_serializer.data, safe=False)
    elif request.method == 'POST':
        studyset_data = JSONParser().parse(request)
        studyset_serializer = StudySetSerializer(data=studyset_data)
        if studyset_serializer.is_valid():
            studyset_serializer.save()
            return JsonResponse(studyset_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(studyset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = StudySet.objects.all().delete()
        return JsonResponse({'message': f'{count[0]} Studysets were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def studyset_details(request, pk):
    # find studyset by pk
    try:
        studyset = StudySet.objects.get(pk=pk)
    except StudySet.DoesNotExist:
        return JsonResponse({'message': 'The studyset does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        studyset_serializer = StudySetSerializer(studyset)
        return JsonResponse(studyset_serializer.data)
    elif request.method == 'PUT':
        studyset_data = JSONParser().parse(request)
        studyset_serializer = StudySetSerializer(studyset, data=studyset_data)
        if studyset_serializer.is_valid():
            studyset_serializer.save()
            return JsonResponse(studyset_serializer.data)
        return JsonResponse(studyset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        studyset.delete()
        return JsonResponse({'message': 'Studyset was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


## Other pages
def index(request):
    return HttpResponse("Hello, world. You're welcome to DigestAI.")

def summarize(request):
    return HttpResponse("Summarize page.")

def create_summary(request):
    return HttpResponse("Create new summary!")

def login(request):
    return HttpResponse("Login page")

def signup(request):
    return HttpResponse("signup page")

def library(request):
    return HttpResponse("library page")

def activity(request):
    return HttpResponse("activity page")

def account(request):
    return HttpResponse("account page")

def studyset(request):
    return HttpResponse("Study Set page")

def info(request):
    return HttpResponse("Info page")
