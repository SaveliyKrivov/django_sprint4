from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='create_post'),
    path('posts/<int:post_id>/edit/',
         views.PostUpdateView.as_view(), name='edit_post'),
    path('posts/<int:post_id>/delete/',
         views.PostDeleteView.as_view(), name='delete_post'),
    path('posts/<int:post_id>/comment/', views.add_comment,
          name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.edit_comment, name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('category/<slug:category_slug>/',
         views.CategoryListView.as_view(), name='category_posts'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), 
         name='edit_profile'),
    path('profile/<slug:username>/',
         views.ProfileDetailView.as_view(), name='profile'),
]
