from .models import Post, Api
from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    in_stock = serializers.BooleanField()


class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "text",
            "comment_count",
        ]

    def get_comment_count(self, obj):
        return obj.comments.count()


class ApiSerializer(serializers.ModelSerializer):
    pass

