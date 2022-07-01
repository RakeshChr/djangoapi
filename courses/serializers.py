from rest_framework import serializers
from .models import Course

# Added Hyperlinked Serializer
class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'url', 'name', 'laguage', 'price')