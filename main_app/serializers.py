from rest_framework import serializers
from .models import Coffee, Feeding, Flavor

# 1. Flavor Serializer remains mostly the same
class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = '__all__'

class CoffeeSerializer(serializers.ModelSerializer):
    fed_for_today = serializers.SerializerMethodField()
    # 2. Add flavors field to show nested flavor data
    flavors = FlavorSerializer(many=True, read_only=True)

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