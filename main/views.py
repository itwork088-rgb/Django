from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .form import ContactForm, PostForm, CharacterForm
from .models import Character

POSTS = [
    {"id": 1, "title": "Ноутбук"},
    {"id": 2, "title": "Мышка"},
    {"id": 3, "title": "Клавиатура"},
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
    return HttpResponse("Пост не найден", status=404)

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

def register_view(request):
    if request.method == "POST":  
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")  
    else:
        form = UserCreationForm()

    return render(request, "blog/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "blog/login.html", {"form": form})
    
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required(login_url="login")
def dashboard_view(request):
    return render(request, "blog/dashboard.html")

def postFormViews(request):
    success_message = ""
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            success_message = "Успешно создан пост"
            post = PostForm()
    else:
        post = PostForm()
    return render(request, 'blog/postmodel.html', {"post" : post, "success_message" : success_message})

def reg(request):
    success_message = ""
    char = Character.objects.all()
    if request.method == "POST":
        character = CharacterForm(request.POST)
        if character.is_valid():
            character.save()
            success_message = "Успешно создан персонаж"
            character = CharacterForm()
    else:
        character = CharacterForm()
    return render(
        request,
        "blog/postmodel.html",
        {
            "allChar" : char,
            "characters": character,
            "success_message": success_message,
        },
    )
    
PRODUCTS = [
    {"id": 1, "title": "ноутбук"},
    {"id": 2, "title": "мышка"},
    {"id": 3, "title": "клавиатура"},
    {"id": 4, "title": "АЙфон"},
    {"id": 5, "title": "Телефон"},
    {"id": 6, "title": "Часы"},
    {"id": 7, "title": "Айрподтс"}
]

NOTES = []


def product_detail(request, product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return HttpResponse(f"Товар: {product['title']}")
    return HttpResponse("Товар не найден")


def search_products(request):
    q = request.GET.get("q", "")
    results = [product for product in PRODUCTS if q.lower() in product["title"].lower()]
    return render(request, "blog/search.html", {"results": results, "q": q})


def create_note(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if text:
            NOTES.append(text)
        return redirect("note_success")
    return render(request, "blog/create_note.html")


def note_success(request):
    return HttpResponse("Данные успешно отправлены")


TASKS = [
    {"id": 1, "title": "сделать дз"},
    {"id": 2, "title": "помыть посуду"},
    {"id": 3, "title": "покормить кота"}
]

NOTES = []


def task_detail(request, product_id):
    for task in TASKS:
        if task["id"] == product_id:
            return HttpResponse(f"Задача: {task['title']}")
    return HttpResponse("Задача не найдена", status=404)



def search(request):
    q = request.GET.get("q", "")
    results = [task for task in TASKS if q.lower() in task["title"].lower()]
    return render(request, "blog/search.html", {"results": results, "q": q})


def task(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if text:
            NOTES.append(text)
        return redirect("seka")
    return render(request, "blog/tasks.html")


def seka(request):
    return HttpResponse("Задачи успешно созданы")




 