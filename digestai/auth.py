from magic_admin import Magic
# A util provided by `magic_admin` to parse the auth header value.
from magic_admin.utils.http import parse_authorization_header_value
from magic_admin.error import DIDTokenError
from magic_admin.error import RequestError

from django.http import HttpResponse, HttpResponseBadRequest
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


def user_signup(request):
    if request.method == 'POST':
        header_token = request.headers['Authorization']
        print(f"DIDToken: \t{header_token}")
        did_token = parse_authorization_header_value(header_token)
        if did_token is None:
            did_token = header_token
            #return HttpResponseBadRequest(
            #    'Authorization header is missing or header value is invalid',
            #)

        magic = Magic(api_secret_key='pk_live_207A0EF93ABE0D60')

        # Validate the did_token.
        try:
            magic.Token.validate(did_token)
            issuer = magic.Token.get_issuer(did_token)
            user_meta = magic.User.get_metadata_by_issuer(issuer)
        except DIDTokenError as e:
            return HttpResponseBadRequest('DID Token is invalid: {}'.format(e))
        except RequestError as e:
            # You can also remap this error to your own application error.
            return HttpError(str(e))

        user_data = JSONParser().parse(request)
        
        #if user_meta.data['email'] != email:
        #    return UnAuthorizedError('UnAuthorized user signup')
        print(user_data)
        # Call your application logic to save the user.
        #logic.User.add(name, email, issuer)

        return JsonResponse(user_data)
    return HttpResponse('User signup page')
