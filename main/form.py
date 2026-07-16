from django import forms
from .models import Character

# Форма обратной связи для contact_view
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Ваш Email")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")

# Форма создания персонажа для функции reg
class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'  # Выводит все поля модели Character в форму
