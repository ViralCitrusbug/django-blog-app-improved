from ast import Str
from rest_framework import serializers
from blogapp.models import Post, Profile,User
from django.contrib.auth.hashers import make_password

class PostSerializers(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields=['title','post_image','content','category',"id","user","soft_delete"]
    def create(self,validated_data):
        new_post = Post.objects.create(**validated_data)
        new_post.user = validated_data['user']
        new_post.save()
        return new_post

    def update(self, post, validated_data):
        new_post = Post(**validated_data)
        new_post.user = post.get('user')
        new_post.id = post.get('id')
        new_post.save()
        return new_post


class UserSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)


    def create(self, validated_data):
        # user = User.objects.create(**validated_data)
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        user_name = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        query = f"INSERT INTO auth_user(first_name, last_name,username,email,password,is_superuser,is_staff,is_active,date_joined)\
                  VALUES    ('{first_name}','{last_name}','{user_name}','{email}','{password}','1','0','1','2022-03-11 11:16:00+05:30');"
        user = User.objects.raw(query)
        user = user.__dict__
        value = str(user.get('raw_query')).split('VALUES')[1].replace(';',"").replace("(","").replace(")","").split(',')
        key = str(user.get('raw_query')).split('VALUES')[0].split('(')[1].replace(')',"").split(',')
        new_user = dict(zip(key,value))
        return new_user

    def update(self, user, validated_data):
        new_user = User(**validated_data)
        new_user.id = user.get('id')
        new_user.save()
        return new_user

        
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Profile
        fields = ['picture','user','id']

    def create(self, validated_data):
        return super().create(**validated_data)  

    def update(self, profile, validated_data):
        new_profile = Profile(**validated_data)
        new_profile.user = profile.get('user')
        new_profile.id = profile.get('id')
        new_profile.save()
        return new_profile