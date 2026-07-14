from django import forms
from .models import Post, Character

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "views"]

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ["name", "hp", "speed"]

