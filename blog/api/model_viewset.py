from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from blogapp.models import Post
from.serializers import *

class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(soft_delete=False)
    serializer_class = PostSerializers
    authentication_class = [TokenAuthentication]
    