
from django.http import HttpResponse

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from digestai.models import StudySet
from digestai.serializers import StudySetSerializer
from rest_framework.decorators import api_view

from magic_admin import Magic
# A util provided by `magic_admin` to parse the auth header value.
from magic_admin.utils.http import parse_authorization_header_value
from magic_admin.error import DIDTokenError
from magic_admin.error import RequestError


# API views
@api_view(['GET', 'POST', 'DELETE'])
def studyset_list(request):
    # GET list of studysets, post a new studyset, delete all studysets
    if request.method == 'GET':
        studysets = StudySet.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            studysets = StudySet.filter(title_icontains=title)

        studysets_serializer = StudySetSerializer(studysets, many=True)
        return JsonResponse(studysets_serializer.data, safe=False)
    elif request.method == 'POST':
        studyset_data = JSONParser().parse(request)
        # generate quiz and flashcards
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

@api_view(['POST'])
def register(request):
    did_token = parse_authorization_header_value(
        requests.headers.get('Authorization'),
    )
    if did_token is None:
        raise BadRequest(
            'Authorization header is missing or header value is invalid',
        )

    magic = Magic(api_secret_key='pk_live_207A0EF93ABE0D60')

    # Validate the did_token.
    try:
        magic.Token.validate(did_token)
        issuer = magic.Token.get_issuer(did_token)
        user_meta = magic.User.get_metadata_by_issuer(issuer)
    except DIDTokenError as e:
        raise BadRequest('DID Token is invalid: {}'.format(e))
    except RequestError as e:
        # You can also remap this error to your own application error.
        return HttpError(str(e))

    return HttpResponse(user_meta)

    # user_data = JSONParser().parse(request)

    #if user_meta.data['email'] != user_data['email']:
    #    return UnAuthorizedError('UnAuthorized user signup')

    #user_serializer = UserSerializer(data=user_data)
    #if user_serializer.is_valid():
    #    user_serializer.save()
    #    return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
    
    #return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def user_details(request):
    if request.method == 'GET':
        return JsonReponse()
    elif request.method == 'POST':
        return JsonResponse()
    elif request.method == 'PUT':
        return JsonResponse()
    return JsonResponse()

@api_view(['POST'])
def summarize(request):
    if request.method == 'POST':
        return JsonResponse()
    return JsonResponse()

@api_view(['GET'])
def generate_flashcards(request):
    if request.method == 'GET':
        return JsonResponse()
    return JsonResponse()

@api_view(['GET', 'POST'])
def generate_quiz(request):
    if request.method == 'GET':
        return JsonResponse()
    elif request.method == 'POST':
        return JsonResponse()
    return JsonResponse()

@api_view(['GET', 'POST'])
def evaluate_quiz(request):
    if request.method == 'GET':
        return JsonResponse()
    elif request.method == 'POST':
        return JsonResponse()
    return JsonResponse()


"""
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

def index(request):
    return HttpResponse("Hello, world. You're welcome to DigestAI.")

def create_summary(request):
    return HttpResponse("Create new summary!")

def login(request):
    return HttpResponse("Login page")
"""
