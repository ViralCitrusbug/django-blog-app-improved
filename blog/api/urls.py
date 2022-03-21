"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django import views
from django.urls import path,include
from .import generic_serialize_view,serialize_view,serialize_classview,model_viewset
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView  , TokenVerifyView
# from rest_framework import 
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('post',model_viewset.PostViewSet,basename="post")


urlpatterns = [

    ##  API FUNCTION BASED VIEWS

    # path('api/post-list',serialize_view.post_list,name="api-postlist"),
    # path('api/users',serialize_view.user_list,name="api-user_list"),
    # path('api/user/<pk>',serialize_view.user_crud,name="api-user-crud"),
    # path('api/profile/<pk>',serialize_view.profile_crud,name="api-profile-crud"),

    ## API CLASS BASED VIEWS (CUSTOM VIEWS)
    
    path('post-list',serialize_classview.PostListView.as_view(),name="api-postlist"),
    path('user-list',serialize_classview.UserListView.as_view(),name="api-userlist"),
    path('user/<pk>',serialize_classview.UserCRUD.as_view(),name="api-user-crud"),
    path('profile-list',serialize_classview.ProfileList.as_view(),name="api-profile_list"),
    path('profile/<pk>',serialize_classview.ProfileCRUD.as_view(),name="api-profile-crud"),
    path('post/<pk>',serialize_classview.PostCRUD.as_view(),name="api-post-crud"),

    ## API GENERIC CLASS BASED VIEWS

    # path('api/post-list',generic_serialize_view.PostListView.as_view(),name="api-postlist"),
    # path('api/user-list',generic_serialize_view.UserListView.as_view(),name="api-userlist"),
    # path('api/user/<pk>',generic_serialize_view.UserCRUD.as_view(),name="api-user-crud"),
    # path('api/profile-list',generic_serialize_view.ProfileListView.as_view(),name="api-profile_list"),
    # path('api/profile/<pk>',generic_serialize_view.ProfileCRUD.as_view(),name="api-profile-crud"),
    # path('api/post/<pk>',generic_serialize_view.PostCRUD.as_view(),name="api-post-crud"),

    ## GENERIC CLASS BASED VIEW

    # path('post-list',generic_serialize_view.PostListView.as_view(),name="api-postlist"),
    # path('user-list',generic_serialize_view.UserListView.as_view(),name="api-userlist"),
    # path('user/<pk>',generic_serialize_view.UserCRUD.as_view(),name="api-user-crud"),
    # path('profile-list',generic_serialize_view.ProfileListView.as_view(),name="api-profile_list"),
    # path('profile/<pk>',generic_serialize_view.ProfileCRUD.as_view(),name="api-profile-crud"),
    # path('post/<pk>',generic_serialize_view.PostCRUD.as_view(),name="api-post-crud"),

    ## SIMPLE JWT TOKEN 

    path('get-jwt-token/',TokenObtainPairView.as_view(),name="obtain-token"),
    path('token-refresh',TokenRefreshView.as_view(),name="refresh-token"),
    path('token-verify',TokenVerifyView.as_view(),name="verify-token")
]

# urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)