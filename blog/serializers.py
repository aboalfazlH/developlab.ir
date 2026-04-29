from rest_framework.serializers import ModelSerializer
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("title","summary","description","thumbnail","is_active","is_verify","is_pin","author","write_date","update_date","get_absolute_url")