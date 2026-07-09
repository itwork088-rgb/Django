from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import ContactForm

POSTS = [
    {"id": 1, "title": "Первый пост"},
    {"id": 2, "title": "Второй пост"},
    {"id": 3, "title": "Третий пост"},
]


def home(request):
    posts = [
        {"author": "Python", "published": True},
        {"title": "Django", "published": True},
    ]

    context = {
        "page_title": "Мой блог",
        "posts": posts,
    }

    return render(request, "blog/home.html", context)


def contacts(request):
    return HttpResponse("Это contacts страница")

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
    



def contact_view(request):
    success_message = ""

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():  
            success_message = "Форма отправлена"
            form = ContactForm()

    else:
        form = ContactForm()

    
    return render(
        request,
        "blog/contact.html",
        {"form": form, "success_message": success_message},
    )
            