from .models import StudentModel
from rest_framework import serializers

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        # fields = ('name', 'st_id', 'level', 'program', 'type')
        fields = '__all__'
