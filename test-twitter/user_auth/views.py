from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import permissions
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from knox.settings import CONSTANTS
from tweets.models import User_profile
from tweets.serializers import User_profileSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class SignupView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        result = User.objects.all()
        all_users = UserSerializer(result, many=True)
        return Response(all_users.data)

    def post(self, request):
        # pulls all of the user data from the request
        data = self.request.data
        username = data["username"]
        email = data["email"]
        password = data["password"]
        re_password = data["re_password"]
        # avatar = data["avatar"]
        # x = "hello"

        try:
            # check and see if the password matches the verification
            if password == re_password:
                # check and see if the username already exists in th e database
                if User.objects.filter(username=username).exists():
                    return Response({"error": "Username already exists"})
                else:
                    # if the user doesn't already exist, create them using the data from the post request
                    user = User.objects.create_user(
                        username=username, password=password)
                    User_profile.objects.create(
                        user=user, email=email, name=username, avatar="None")
                    print(User_profile)

                    response = Response({
                        "success": "User created successfully",
                        # creates an authtoken for the user
                        "token": AuthToken.objects.create(user)[1]
                    })
                    response.set_cookie(
                        "sa_token", AuthToken.objects.create(user)[1])
                    return response
            else:
                return Response({"error": "Passwords do not match"})
        except:
            return Response({"error": "Something went wrong signing up"})


class LoginView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        data = self.request.data
        username = data["username"]
        password = data["password"]
        try:
            # checks if username and password are correct
            user = auth.authenticate(username=username, password=password)

            # if the user exists, tries to login
            if user is not None:
                auth.login(request, user)
                response = Response({"success": "User authenticated",
                                     # creates an authtoken for the user
                                     "token": AuthToken.objects.create(user)[1]})

                response.set_cookie(
                    "sa_token", AuthToken.objects.create(user)[1])
                return response
            else:
                return Response({"error": "Error Authenticating"})
        except:
            return Response({"error": "Something went wrong when logging in"})


class GrabProfile(APIView):
    def get(self, request):
        try:
            user = self.request.user
            # grabs the profile from the database that matches the requested user
            profile = User_profile.objects.get(user=user)

            # converts the profile to JSON
            profile_json = User_profileSerializer(profile)
            return Response({"profile": profile_json.data})
        except:
            return Response({"error": "no user profile found"})

# class Verify(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     def post(self, request, format=None):
#         knox_object = AuthToken.objects.filter(token_key=request.COOKIES["sa_token"][:CONSTANTS.TOKEN_KEY_LENGTH]).first()
#         print(knox_object)
#         return Response('hi')


class Verify(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        objs = AuthToken.objects.filter(
            token_key=request.COOKIES["sa_token"][:CONSTANTS.TOKEN_KEY_LENGTH])
        if len(objs) == 0:
            return None

        # return Response({"user": objs.first().user})
        user = objs.first().user
        profile = User_profile.objects.get(user=user)
        profile_json = User_profileSerializer(profile)
        print(profile_json)
        return Response(profile_json.data)
