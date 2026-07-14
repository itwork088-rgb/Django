from django.contrib import admin
from .models import Post, Comment, Book, Author, State, Character, Student

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(State)
admin.site.register(Character)

from django.contrib import admin
from .models import Pot


@admin.register(Student)
class PotAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "grade", "profession", "age", "in_study")
    list_filter = ("grade", "in_study")
    search_fields = ("name",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)



