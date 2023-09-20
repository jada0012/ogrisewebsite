from time import process_time_ns
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView
from .models import Post, Resource, Engage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
# Create your views here.
def home(response):
    return render(response, 'blog/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'blog/articles.html'

class ResourcesView(ListView):
    model = Resource
    template_name = 'blog/resources.html'
class EngageView(ListView):
    model = Engage
    template_name = 'blog/getengaged.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/individualarticle.html'

class EngageDetailView(DetailView):
    model = Engage
    template_name = 'blog/individualengage.html'

class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'blog/individualresource.html'

@method_decorator(login_required, name='dispatch')
class AddPostView(CreateView):
    model = Post
    template_name = 'blog/addpost.html'
    fields = ['title', 'author', 'body', 'slug']

# @method_decorator(superuser_required,name='dispatch')
class UnauthenticatedPostView(ListView):
    model = Post
    template_name = 'blog/unauthpost.html'

def showRecentArticles(response):
    posts = Post.objects.filter().order_by('-created_on')[0:4]
    return render(response, 'blog/recentarticles.html', {'posts':posts})

def test(response):
    return render(response, 'blog/test.html', {})
