from rest_framework import serializers
from .models import Shape

class AppSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')
    class Meta:
        model = Shape
        fields = "__all__"
        
    def get_days_since_joined(self, obj):
        return 'additional'