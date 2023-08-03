from rest_framework import serializers
from .models import timing_model,RegisterModel

class registe_serializers(serializers.ModelSerializer):
    class Meta:
        model=RegisterModel
        fields=("id",'emp','name','date')

class timing_serializers(serializers.ModelSerializer):
    emp=registe_serializers(read_only=True)
    duration=serializers.SerializerMethodField()
    def get_duration(self,obj):
        return obj.duration() 
    class Meta:
        model=timing_model
        fields=['id','clock_in','clock_out','duration','emp']