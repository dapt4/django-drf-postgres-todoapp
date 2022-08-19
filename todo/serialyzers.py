from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        read_only = True,
        slug_field = 'username'
    )
    class Meta:
        model = Todo
        fields = ['id','title', 'done', 'created_at', 'user']