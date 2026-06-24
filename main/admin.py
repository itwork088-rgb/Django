from django.contrib import admin
from .models import Post, Comment, Book, Author, State, Character

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(State)
admin.site.register(Character)
