
from django.http import HttpResponse
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from digestai.models import StudySet, User
from digestai.serializers import StudySetSerializer
from rest_framework.decorators import api_view

from magic_admin import Magic
# A util provided by `magic_admin` to parse the auth header value.
from magic_admin.utils.http import parse_authorization_header_value
from magic_admin.error import DIDTokenError
from magic_admin.error import RequestError

from django.core.cache import cache


# API views
@api_view(['GET', 'POST', 'DELETE'])
def studyset_list(request):
    # GET list of studysets, post a new studyset, delete all studysets
    if request.method == 'GET':
        # Get email from auth token
        # email = 'prof.chakas@gmail.com'
        email = 'chansa.k@turing.com'
        try:
            user = User.objects.filter(email=email)[0]
        except:
            return JsonResponse({'message': f'user for {email} not found!'}, status=status.HTTP_204_NO_CONTENT)
        
        studysets = cache.get(user.email, 'expired')
        if studysets == 'expired':
            studysets = StudySet.objects.filter(username=user.username)
            cache.set(user.email, studysets, timeout=60)

        studysets_serializer = StudySetSerializer(studysets, many=True)
        return JsonResponse(studysets_serializer.data, safe=False)
    elif request.method == 'POST':
        studyset_data = JSONParser().parse(request)
        print(type(studyset_data), studyset_data)
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

    #user_data = JSONParser().parse(request)

    #if user_meta.data['email'] != user_data['email']:
    #    return UnAuthorizedError('UnAuthorized user signup')

    #user_serializer = UserSerializer(data=user_data)
    #if user_serializer.is_valid():
    #    user_serializer.save()
    #    return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
    
    #return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(user_meta)


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
