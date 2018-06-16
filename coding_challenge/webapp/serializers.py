from rest_framework import serializers
from rest_framework import test

class testSerializer(serializers.ModelSerializer):

	class Meta:
		model = test
		#fields = ('firstname', 'lastname')
		#fields = '__all__'