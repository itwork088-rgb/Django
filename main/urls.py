from django.urls import path
from .views import post_detail, home, AboutView, contacts

urlpatterns = [
    path("posts/<int:post_id>/", post_detail, name="post_detail"),
    path('', home, name='home'),
    path('contact/', contacts, name='contacts'),
    path("about/", AboutView.as_view(), name="about")
]
