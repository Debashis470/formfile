from rest_framework import serializers
from .models import Perasonalinfo

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perasonalinfo
        fields = '__all__'