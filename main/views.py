from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer, PostSerializer
from .models import Character, Post, Api

# --- Описание форм прямо во views.py ---

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Ваш Email")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

# --- Временные базы данных ---
POSTS = [
    {"id": 1, "title": "Ноутбук"},
    {"id": 2, "title": "Мышка"},
    {"id": 3, "title": "Клавиатура"},
]

PRODUCTS = [
    {"id": 1, "title": "Ноутбук", "price": 300000, "in_stock": True},
    {"id": 2, "title": "Мышка", "price": 7000, "in_stock": False},
    {"id": 3, "title": "клавиатура"},
    {"id": 4, "title": "АЙфон"},
    {"id": 5, "title": "Телефон"},
    {"id": 6, "title": "Часы"},
    {"id": 7, "title": "Айрподтс"}
]

TASKS = [
    {"id": 1, "title": "сделать дз"},
    {"id": 2, "title": "помыть посуду"},
    {"id": 3, "title": "покормить кота"}
]

NOTES = []

# --- Стандартные Django Views ---

def home(request):
    posts = [
        {"author": "Python", "published": True},
        {"title": "Django", "published": True},
    ]
    context = {
        "page_title": "Мой blog",
        "posts": posts,
    }
    return render(request, "blog/home.html", context)

def contacts(request):
    return HttpResponse("Это contacts страница")

def news(request):
    return HttpResponse("Это news страница")

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
        request, "blog/contact.html", {"form": form, "success_message": success_message}
    )

# --- Авторизация и регистрация пользователей ---

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

# --- Работа с моделями ---

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
            "allChar": char,
            "characters": character,
            "success_message": success_message,
        },
    )

# --- Логика для Продуктов, Заметок и Задач ---

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

# --- Django REST Framework (API) ---

class ProductListAPIView(APIView):
    def get(self, request):
        serializer = ProductSerializer(PRODUCTS, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
