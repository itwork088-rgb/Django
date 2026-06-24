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
    state = models.OneToOneField(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name