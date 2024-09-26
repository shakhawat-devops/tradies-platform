import os
from dotenv import load_dotenv
from django.http import HttpResponse
import requests
from services_app.utils import CustomUser

load_dotenv()


class UserData(object):
    is_authenticated = True

    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

class CustomAuthMiddleware:
    def __init__(self, get_response):
        AUTH_URL = os.getenv("AUTH_SERVICE_URL", "http://host.docker.internal:8000")

        self.get_response = get_response
        self.auth_service_url = f"{AUTH_URL}/api/v1/token/verify/"

    def __call__(self, request):

        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            return HttpResponse("Unauthorize: No header", status=401)

        token = auth_header.split(" ")[1]

        # Send a request to the authentication service to verify the token
        auth_response = requests.post(self.auth_service_url, json={"token": token})

        if auth_response.status_code == 200:
            # Token is valid, proceed with the request
            # request.user = {"name": "Dinesh", "username": "admin"}
            user_data = auth_response.json().get('user')

            print("User data: ", user_data)
            if(user_data):
                request._user = UserData(user_data)

            print("request user: ", request._user)

            response = self.get_response(request)

            print("request", request.user.id)

            print('response in asdfasdf: ', response)

            return response
        else:
            # Token is invalid, deny access
            return HttpResponse("Unauthorized: Invalid Token", status=401)
