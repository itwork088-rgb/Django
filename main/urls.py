from django.urls import path
from .views import (
    home, AboutView, ServicesViews, contacts, 
    contact_view, register_view, login_view, logout_view, 
    dashboard_view, reg, 
    search_products, create_note, note_success, task_detail, search, task, seka, ProductListAPIView, PostListAPIView
)

urlpatterns = [
    path('contact_view/', contact_view, name='contact_view'),
    path('', home, name='home'),
    path('contact/', contacts, name='contacts'),
    path("about/", AboutView.as_view(), name="about"),
    path("service/", ServicesViews.as_view(), name="service"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("reg/", reg, name="reg"),
    path("search/", search_products, name="search_product"),
    path("notes/create/", create_note, name="create_note"),
    path("notes/success/", note_success, name="note_success"),
    path("task_detail", task_detail, name="task_detail_flat"),
    path("searching", search, name="searching"),
    path("task/", task, name="tasks"),
    path("seka/", seka, name="seka"),
    path("api/products/", ProductListAPIView.as_view(), name="api_products"),
    path("api/posts", PostListAPIView.as_view(), name="api_posts")
]


