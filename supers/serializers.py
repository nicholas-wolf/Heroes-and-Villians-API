from rest_framework import serializers
from .models import Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secodary_ability', 'catchphrase', 'super_type_id']
        depth = 1

    supur_type_id = serializers.IntegerField(write_only=True)    