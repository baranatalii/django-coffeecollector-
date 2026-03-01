from rest_framework import serializers
from .models import Coffee, Feeding

class CoffeeSerializer(serializers.ModelSerializer):
    fed_for_today = serializers.SerializerMethodField()

    class Meta:
        model = Coffee
        fields = '__all__'

    def get_fed_for_today(self, obj):
        return obj.fed_for_today()

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'
        read_only_fields = ('coffee',)