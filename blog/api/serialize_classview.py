import re
from blogapp.models import Post,Profile
from django.contrib.auth.models import User
from .serializers import UserSerializer,PostSerializers,ProfileSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

class PostListView(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        post = Post.objects.all()
        serialize = PostSerializers(post,many=True)
        return Response(serialize.data)
    
    def post(self,request):
        serialize = PostSerializers(data=request.data)
        if serialize.is_valid():
            return Response(serialize.data)
        else:
            return Response(serialize.errors)

class UserListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = User.objects.raw("SELECT * FROM auth_user")
        serialize = UserSerializer(user,many=True)
        return Response(serialize.data)
    
    def post(self,request):
        data = {}
        data['first_name']=request.data.get('first_name')
        data['last_name']=request.data.get('last_name')
        data['username']=request.data.get('username')
        data['email']=request.data.get('email')
        data['password']=request.data.get('password')
        print(data)
        serialize = UserSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            print("#########################################################")
            return Response("DOne")
        else:
            return Response(serialize.errors)

class UserCRUD(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classed = [IsAdminUser]
    def get_user(self,pk):
        try:
            query = f"SELECT * FROM auth_user WHERE auth_user.id = '{pk}'"
            user = User.objects.raw(query)
            return user
        except User.DoesNotExist:
            return False
    
    def get(self,request,pk):
        if self.get_user(pk):
            query = f"SELECT * FROM auth_user WHERE auth_user.id = '{pk}'"
            response = {}
            user = User.objects.raw(query)
            for i in user:
                response['username'] = i.username
                response['id'] = i.id
                response['first_name'] = i.first_name
                response['last_name'] = i.last_name
                response['email'] = i.email
            serialize = UserSerializer(response)
            return Response(serialize.data)
        else:
            return Response("User Doesn't Exist")
    def put(self,request,pk):
        if self.get_user(pk):
            query = f"SELECT * FROM auth_user WHERE auth_user.id = '{pk}'"
            response = {}
            user = User.objects.raw(query)
            for i in user:
                response['username'] = i.username
                response['id'] = i.id
                response['first_name'] = i.first_name
                response['last_name'] = i.last_name
                response['email'] = i.email
            serializer = UserSerializer(response,data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data)
            else:
                return Response(serializer.errors)          
        else:
            return Response("User Doesn't Exist")
    
class ProfileList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        profile = Profile.objects.all()
        serialize = ProfileSerializer(profile,many=True)
        return Response(serialize.data)

class ProfileCRUD(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def get_profile(self,pk):
        try:
            query = f"SELECT * FROM blogapp_profile where blogapp_profile.id={pk}"
            profile = Profile.objects.raw(query)
            return profile
        except Profile.DoesNotExist:
             return False
    
    def get(self,request,pk):
        if self.get_profile(pk):
            query = f"SELECT * FROM blogapp_profile WHERE blogapp_profile.id = '{pk}'"
            response = {}
            user = Profile.objects.raw(query)
            for i in user:
                print(i.picture)
                response['user'] = i.user
                response['id'] = i.id
                response['picture']=i.picture
            print(response)
            serialize = ProfileSerializer(response)
            print(serialize.data)
            return Response(serialize.data)
        else:
            return Response("Profile Doesn't Exist")
    
    def put(self,request,pk):
        if self.get_profile(pk):
            query = f"SELECT * FROM blogapp_profile where blogapp_profile.id={pk}"
            response = {}
            profile = Profile.objects.raw(query)
            for i in profile:
                response['user']=i.user
                response['picture']=i.picture
                response['id']=i.id
            serializer = ProfileSerializer(response,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Profile Not Found")


class PostCRUD(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def get_post(self,pk):
        try:
            query = f"SELECT * FROM blogapp_post where blogapp_post.id={pk}"
            post = Post.objects.raw(query)
            return post
        except Post.DoesNotExist:
            return False
    
    def get(self,request,pk):
        if self.get_post(pk):
            query = f"SELECT * FROM blogapp_post WHERE blogapp_post.id = '{pk}'"
            response = {}
            post = Post.objects.raw(query)
            print("*************************")
            for i in post:
                response['title'] = i.title
                response['content'] = i.content
                response['post_image']=i.post_image
                response['user']=i.user
                response['id']=i.id
            print(response)
            serialize = PostSerializers(response)
            print(serialize.data)
            return Response(serialize.data)
        else:
            return Response("Post Doesn't Exist")
    
    def put(self,request,pk):
        if self.get_post(pk):
            query = f"SELECT * FROM blogapp_post WHERE blogapp_post.id = '{pk}'"
            response = {}
            post = Post.objects.raw(query)
            for i in post:
                response['title'] = i.title
                response['content'] = i.content
                response['post_image']=i.post_image
                response['user']=i.user
                response['id']=i.id
            print(1)
            serializer = PostSerializers(response,data = request.data)
            print(2)
            if serializer.is_valid():
                print(3)
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Post Doesn't Exist")