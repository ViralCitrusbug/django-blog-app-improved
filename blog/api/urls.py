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
from django.urls import path
from .import generic_serialize_view,serialize_view,serialize_classview


urlpatterns = [
    path('post-list',generic_serialize_view.PostListView.as_view(),name="api-postlist"),
    path('user-list',generic_serialize_view.UserListView.as_view(),name="api-userlist"),
    path('user/<pk>',generic_serialize_view.UserCRUD.as_view(),name="api-user-crud"),
    path('profile-list',generic_serialize_view.ProfileListView.as_view(),name="api-profile_list"),
    path('profile/<pk>',generic_serialize_view.ProfileCRUD.as_view(),name="api-profile-crud"),
    path('post/<pk>',generic_serialize_view.PostCRUD.as_view(),name="api-post-crud"),
]

# urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)