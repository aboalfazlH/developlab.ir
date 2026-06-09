from rest_framework.serializers import ModelSerializer
from .models import Post,PostComment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("title","summary","description","thumbnail","is_active","is_pin","author","write_date","update_date","get_absolute_url")
    
class PostCommentSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = ("user","reply_to","content","write_date","edited","is_active")