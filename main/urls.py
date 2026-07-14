from django.urls import path
from .views import (
    post_detail, home, AboutView, ServicesViews, contacts, 
    contact_view, register_view, login_view, logout_view, 
    dashboard_view, postFormViews, reg, product_detail, 
    search_products, create_note, note_success, task_detail, search, task, seka
)

urlpatterns = [
    path('contact_view/', contact_view, name='contact_view'),
    path("posts/<int:post_id>/", post_detail, name="post_detail"),
    path('', home, name='home'),
    path('contact/', contacts, name='contacts'),
    path("about/", AboutView.as_view(), name="about"),
    path("service/", ServicesViews.as_view(), name="service"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("postmake/", postFormViews, name="createpost"),
    path("reg/", reg, name="reg"),  

    path("products/<int:product_id>/", product_detail, name="product_detail"),
    path("search/", search_products, name="search_product"),
    path("notes/create/", create_note, name="create_note"),
    path("notes/success/", note_success, name="note_success"),
    path("task_detail", task_detail, name="task_detail_flat"),
    path("searching", search, name="searching"),
    path("task/", task, name="tasks"),
    path("seka/", seka, name="seka")
]

