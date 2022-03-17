import re
from django.http import JsonResponse
from rest_framework import mixins,generics
from django.db.models import Q
from blogapp.models import Post,Profile
from .serializers import PostSerializers, ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser    
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from .mypagination import MyPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


class PostListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Post.objects.raw('SELECT * from blogapp_post where soft_delete = False')
    # queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        category = request.GET.get('category')
        search = request.GET.get('search')
        if category:
            query = f'SELECT*FROM blogapp_post LEFT JOIN blogapp_category ON blogapp_post.category_id = blogapp_category.id where category_id={category}'
            self.queryset = Post.objects.raw(query)
            print(query)
            for i in self.queryset:
                print(i.id)
        if search:
            query = f"SELECT * FROM blogapp_post where blogapp_post.title like '%{search}%' or blogapp_post.content like '%{search}%'"
            print(query)
            self.queryset = Post.objects.filter(Q(title__icontains=search)|Q(content__icontains=search))
        
        return self.list(request)

    def post(self,request):
        print(request.data)
        request.data.update({'user':request.user.id})
        return self.create(request)

class UserListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = User.objects.raw('SELECT * FROM auth_user')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class UserCRUD(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = User.objects.raw('SELECT * FROM auth_user')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)

class ProfileListView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    # queryset = Profile.objects.raw('SELECT * FROM blogapp_profile')
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        return self.list(request)

class ProfileCRUD(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = ProfileSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    #  def delete(self,request,pk):
    #      return self.destroy(request)

class PostCRUD(generics.GenericAPIView,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
    queryset = Post.objects.raw("SELECT * FROM blogapp_post")
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUser]

    def get_post(self,pk):
        try:
            query = f"SELECT * FROM blogapp_post where blogapp_post.id = {pk}"
            post = Post.objects.raw(query)
            return post
        except Post.DoesNotExist:
            return False

    def get(self,request,pk):
        if self.get_post(pk):
            post = Post.objects.get(pk=pk)
            return self.retrieve(request)
        else:
            return JsonResponse("Post Not Found")

    def put(self,request,pk):
        print("*")
        
        print("*")
        print(request.data)
        print("*")
        return self.update(request)
    
    def delete(self,request,pk):
        return self.retrieve(request)
        

class PostSearchFilter(ListAPIView):
    queryset = Post.objects.filter(soft_delete=False)
    filter_backends = [SearchFilter]
    search_fields = ['content','title']