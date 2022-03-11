from msilib.schema import Class
from django.urls import path

# from ..api import generic_serialize_view
from . import views,classviews

app_name = "blog"

urlpatterns = [
    # path("",views.home,name="home"),
    # path("blog/post/<int:post_id>",views.blog_detail,name="blog-detail"),
    # path('user/<str:username>/profile',views.profile,name="prfile"),
    # path('user/login',views.login,name="login"),
    # path('user/logout',views.logout,name="logout"),
    # path('user/create',views.signup,name="register"),
    # path('blog/<str:id>/comment',views.post_comment,name='post-comment'),
    # path('post/filter/<str:category>',views.post_by_category,name="post-by-category"),
    # path('blog/create',views.add_blog,name='create-blog'),
    # path('blog/<str:id>/delete',views.delete_blog,name="delete-blog"),

    ##  CLASS BASED VIEW

    path('',classviews.PostList.as_view(),name="home"),
    path('blog/post/<int:post_id>',classviews.PostDetail.as_view(),name="post-detail"),
    path('user/create',classviews.CreateUser.as_view(),name="create-user"),
    path('user/<int:pk>/profile',classviews.ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>/update',classviews.ProfileUpdate.as_view()),
    path('blog/<int:pk>/delete',classviews.DeletePost.as_view(),name='delete-blog'),
    path('blog/<str:id>/comment',classviews.PostComment.as_view(),name='post-comment'),
    path('blog/create',classviews.CreatePost.as_view(),name='create-blog'),
    path('user/logout',classviews.Logout.as_view(),name='logout'),
    path('user/login',classviews.Login.as_view(),name='login'),
    path('post/filter/<str:category>',classviews.PostByCategory.as_view(),name="post-by-category"),



]