from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ForeignKey(User, on_delete=models.CASCADE)
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Post
        field = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 
            'created_at', 'updated_at', 'title', 'content', 'image'
            ]