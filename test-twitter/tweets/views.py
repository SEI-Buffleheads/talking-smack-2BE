from rest_framework import viewsets
from .models import User_profile, Comment, Post
from rest_framework.views import APIView
from .serializers import User_profileSerializer, Comment_Serializer, Post_Serializer
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.


class UserProfile_ViewSet(viewsets.ModelViewSet):
    queryset = User_profile.objects.all()
    serializer_class = User_profileSerializer


class All_Comment_ViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Comment_Serializer


class Post_ViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Post_Serializer


class AllPost_ViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        try:
            user = self.request.user
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                content = request.data['content']
                userProfile = User_profile.objects.get(user=user)
                Post.objects.create(user=userProfile, content=content)
                return Response({'message': "Post Successfully Created!"})
            else:
                return Response({'error': "not authenticated make sure you include a token"})
        except:
            return Response({'error': "error; you are most likely messed up by passing an invaild body"})

    def get(self, request):
        try:
            results = Post.objects.all()
            all_post = Post_Serializer(results, many=True)
            return Response(all_post.data)
        except:
            return Response({"error": "something went wrong"})


class OnePost_ViewSet(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request, id):
        try:
            post_results = Post.objects.get(id=id)
            post = Post_Serializer(post_results)
            comments_results = Comment.objects.filter(post=id)
            comments = Comment_Serializer(comments_results, many=True)
            return Response({"post": post.data, "comments": comments.data})
        except:
            return Response({"error": "something went wrong"})

    def put(self, request, id):
        try:
            user = self.request.user
            isAuthenticated = user.is_authenticated
            if isAuthenticated:

                content = request.data['content']
                userProfile = User_profile.objects.get(user=user)
                Post.objects.update(user=userProfile, content=content)
                return Response({'message': "Post Successfully updated!"})
            else:
                return Response({'error': "not authenticated make sure you include a token"})
        except:
            return Response({'error': "error; you are most likely messed up by passing an invaild body"})


class Comment_ViewSet(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request, id):
        try:
            post_results = Post.objects.get(id=id)
            post = Post_Serializer(post_results)
            comments_results = Comment.objects.filter(post=id)
            print(comments_results)
            print(post.data)

            comments = Comment_Serializer(comments_results, many=True)
            print(comments.data)
            return Response({"post": post.data, "comments": comments.data})
        except:
            return Response({"error": "something went wrong"})

    def post(self, request, id):
        try:
            user = self.request.user
            isAuthenticated = user.is_authenticated
            if isAuthenticated:
                content = request.data['content']
                userProfile = User_profile.objects.get(user=user)
                post = Post.objects.get(id=id)
                Comment.objects.create(
                    user=userProfile, content=content, post=post)
                return Response({'message': "Comment Successfully Created!"})
            else:
                return Response({'error': "not authenticated make sure you include a token"})
        except:
            return Response({'error': "error; you are most likely messed up by passing an invaild body"})
