from django.contrib.messages.api import success
from django.urls.base import reverse
from django.views.generic import ListView,TemplateView, CreateView,DetailView,DeleteView
from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
from django.urls import reverse_lazy


class IndexView(ListView):
    model = User
    template_name = "app/index.html"
    context_object_name = 'tweet_list'


class PostCreateView(CreateView):
    model = User
    template_name = "app/post_create.html"
    fields = '__all__'
    
    success_url = reverse_lazy('app:index')

class PostDetailView(DetailView):
    model = User
    context_object_name = 'tweet_list'

    template_name = "app/post_detail.html"


class PostDeleteView(DeleteView):
    model = User
    context_object_name = 'tweet_list'

    template_name = "app/post_delete.html"
    
    success_url = reverse_lazy('app:index')

