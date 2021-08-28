from django.urls import path
from django.views.generic import detail
from django.views.generic.edit import UpdateView
#from . import views
from .views import BlogDetailView, CategoryView, HomeView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    #path('',views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('blog/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:categories>/', CategoryView, name='category'),
]