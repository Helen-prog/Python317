from django.shortcuts import render
from django.views.generic import ListView

from .models import *

menu = [
    {'title': 'Добавить статью', 'url_name': 'index'},
    {'title': 'Войти', 'url_name': 'index'},
]


class BlogHome(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['menu'] = menu
        return context
