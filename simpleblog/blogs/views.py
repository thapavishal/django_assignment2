from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog


class HomeView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blogs/index.html'
    context_object_name = 'blog_entries'
    ordering = ['-date']
    paginate_by = 3


class BlogView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blogs/detail.html'


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blogs/create_blog.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
