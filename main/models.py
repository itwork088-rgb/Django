from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    





class Book(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return super().__str__()
    


class State(models.Model):
    hp = models.IntegerField()
    speed = models.IntegerField()
    mana = models.IntegerField()


class Character(models.Model):
    avatar = models.ImageField(upload_to=("media/user/avatar"))
    name = models.CharField(max_length=50)
    hp = models.IntegerField(default=True, verbose_name="Здоровье")
    speed = models.IntegerField(default=True, verbose_name="Скорость")

    def __str__(self):
        return self.name


from django.db import models


class Pot(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    age = models.IntegerField()
    profession = models.CharField(max_length=50)
    in_study = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
