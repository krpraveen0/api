#serializers for converting the complex data type in python native data contenttypes
# deserialization -- reverse process of serialization.
#importing the serializers form rest_framework
from rest_framework import serializers
from api.models import Students

class StudentSerializer(serializers.Serializer):
    s_no=serializers.IntegerField()
    s_name=serializers.CharField(max_length=60)
    s_course=serializers.CharField(max_length=60)
    course_fee = serializers.FloatField()
    def create(self,validated_data):
        return Students.objects.create(**validated_data)
