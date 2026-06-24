from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

POSTS = [
    {"id": 1, "title": "Первый пост"},
    {"id": 2, "title": "Второй пост"},
    {"id": 3, "title": "Третий пост"},
]


def home(request):
    return HttpResponse("Это главная страница")


def contacts(request):
    return HttpResponse("Это rf страница")

def news(request):
    return HttpResponse("Это news страница")

def post_detail(request, post_id):
    for post in POSTS:
        if post["id"] == post_id:
            return HttpResponse(f"Пост: {post['title']}")

    return HttpResponse("Пост не найден")


class AboutView(View):
    def get(self, request):
        return HttpResponse("Это страница О нас")
    
class AboutView(View):
    def get(self, request):
        return HttpResponse("Это страница О нас")
    
    
class ServicesViews(View):
    def get(self, request):
        return HttpResponse("Это страница services")    