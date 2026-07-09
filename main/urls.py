from django.urls import path
from .views import post_detail, home, AboutView, contacts, contact_view

urlpatterns = [
    path('contact_view/', contact_view, name='contact_view'),
    path("posts/<int:post_id>/", post_detail, name="post_detail"),
    path('', home, name='home'),
    path('contact/', contacts, name='contacts'),
    path("about/", AboutView.as_view(), name="about")
]
