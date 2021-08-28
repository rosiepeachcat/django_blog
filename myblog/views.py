from django.urls.base import reverse_lazy
from myblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name ='home.html'
    ordering = ['-post_date']
    #ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 


def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories.replace('-', ' '))
    return render (request, 'categories.html', {'categories':categories.replace('-', ' '), 'category_posts':category_posts})


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name ='add_post.html'
    #fields ='__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name ='edit_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name ='add_category.html'
    fields ='__all__'